#!/usr/bin/env python3
"""Offline closure for direct LaTeX citations and explicit bibitems; no TeX execution.

This checks keys, not bibliographic truth or support. Dynamic citation macros,
conditional TeX, and external bibliography systems fail closed.
"""
import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

CITES = {'cite', 'citep', 'citet', 'citealt', 'citealp', 'citeauthor',
         'citeyear', 'citeyearpar', 'parencite', 'textcite', 'autocite',
         'footcite', 'smartcite', 'supercite'}
MULTICITES = {'cites', 'parencites', 'textcites', 'autocites', 'footcites'}
LITERAL_START = re.compile(r'\\begin\{(verbatim\*?|Verbatim|lstlisting|minted|comment)\}')
KEY = re.compile(r'[A-Za-z0-9_.:+/\-]+\Z')
DYNAMIC_BODY = re.compile(r'\\(?:' + '|'.join(sorted(CITES | MULTICITES |
                          {'nocite', 'bibitem', 'input', 'include'})) + r')\b')


def blank(text):
    return ''.join('\n' if x == '\n' else ' ' for x in text)


def clean(text):
    # Preserve newlines so every finding retains a useful source line.
    out, p = [], 0
    while p < len(text):
        if text[p] == '%':
            q = text.find('\n', p)
            q = len(text) if q < 0 else q
            out.append(blank(text[p:q]))
            p = q
            continue
        if text[p] == '\\':
            literal = LITERAL_START.match(text, p)
            if literal:
                end = '\\end{' + literal.group(1) + '}'
                q = text.find(end, literal.end())
                if q < 0:
                    raise ValueError('Unclosed literal environment')
                q += len(end)
                out.append(blank(text[p:q]))
                p = q
                continue
            verb = re.match(r'\\verb\*?([^\w\s])', text[p:])
            if verb:
                q = text.find(verb.group(1), p + len(verb.group()))
                if q < 0 or '\n' in text[p:q]:
                    raise ValueError('Unclosed inline verb literal')
                out.append(blank(text[p:q+1]))
                p = q + 1
                continue
            listing = re.match(r'\\lstinline\b', text[p:])
            if listing:
                start = options(text, p + len(listing.group()))
                if start >= len(text):
                    raise ValueError('Missing lstinline literal')
                if text[start] == '{':
                    _, q = group(text, start)
                else:
                    delimiter = text[start]
                    q = text.find(delimiter, start + 1)
                    if q < 0 or '\n' in text[start:q]:
                        raise ValueError('Unclosed lstinline literal')
                    q += 1
                out.append(blank(text[p:q]))
                p = q
                continue
            # Escaped punctuation, including percent, is not a comment.
            if p + 1 < len(text) and not text[p+1].isalpha():
                out.append(text[p:p+2])
                p += 2
                continue
        out.append(text[p])
        p += 1
    return ''.join(out)


def ws(s, p):
    while p < len(s) and s[p].isspace():
        p += 1
    return p


def group(s, p, left='{', right='}'):
    p = ws(s, p)
    if p >= len(s) or s[p] != left:
        raise ValueError('Expected literal ' + left + right + ' argument')
    start, depth = p + 1, 1
    p += 1
    while p < len(s):
        if s[p] == '\\':
            p += 2
            continue
        if s[p] == left:
            depth += 1
        elif s[p] == right:
            depth -= 1
            if depth == 0:
                return s[start:p], p + 1
        p += 1
    raise ValueError('Unclosed ' + left + right + ' argument')


def options(s, p):
    p = ws(s, p)
    if p < len(s) and s[p] == '*':
        p = ws(s, p + 1)
    while p < len(s) and s[p] == '[':
        _, p = group(s, p, '[', ']')
        p = ws(s, p)
    return p


class Checker:
    def __init__(self, root):
        self.root = root
        self.citations, self.entries = defaultdict(list), defaultdict(list)
        self.nocites, self.errors, self.files = [], [], {}
        self.in_bibliography = False
        self.bibliography_count = 0

    def error(self, loc, message):
        self.errors.append(dict(**loc, message=message))

    def keys(self, value, loc):
        keys = [k.strip() for k in value.split(',')]
        if not keys or any(not KEY.fullmatch(k) for k in keys):
            raise ValueError('Citation keys must be literal nonempty keys: ' + value)
        return keys

    def read(self, path, stack=()):
        path = path.resolve()
        loc = {'file':str(path), 'line':1}
        if not path.is_relative_to(self.root):
            self.error(loc, 'Input is outside --root; not read')
            return
        if path in stack:
            self.error(loc, 'Recursive input cycle')
            return
        if not path.is_file():
            self.error(loc, 'Missing local input')
            return
        data = path.read_bytes()
        self.files[str(path)] = hashlib.sha256(data).hexdigest()
        try:
            s = clean(data.decode('utf-8'))
        except (UnicodeDecodeError, ValueError) as exc:
            self.error(loc, 'Cannot safely parse input: ' + str(exc))
            return
        p = 0
        while p < len(s):
            if s[p] != '\\':
                p += 1
                continue
            m = re.match(r'\\([A-Za-z@]+|.)', s[p:])
            if not m:
                break
            cmd, pos = m.group(1), p
            p += len(m.group())
            loc = {'file':str(path), 'line':s.count('\n', 0, pos) + 1}
            try:
                if cmd in {'input', 'include'}:
                    value, p = group(s, p)
                    if any(c in value for c in '\\#{}'):
                        raise ValueError('Dynamic input path unsupported')
                    child = path.parent / value.strip()
                    if not child.suffix:
                        child = child.with_suffix('.tex')
                    self.read(child, (*stack, path))
                elif cmd in {'begin', 'end'}:
                    value, p = group(s, p)
                    if value == 'thebibliography':
                        self.in_bibliography = cmd == 'begin'
                        if cmd == 'begin':
                            self.bibliography_count += 1
                            if self.bibliography_count > 1:
                                self.error(loc, 'Multiple thebibliography environments in one manuscript; audit separate documents separately')
                elif cmd == 'bibitem':
                    value, p = group(s, options(s, p))
                    if not self.in_bibliography:
                        raise ValueError('bibitem outside thebibliography')
                    keys = self.keys(value, loc)
                    if len(keys) != 1:
                        raise ValueError('bibitem requires one key')
                    self.entries[keys[0]].append(loc)
                elif cmd in CITES or cmd == 'nocite':
                    value, p = group(s, options(s, p))
                    if cmd == 'nocite':
                        self.nocites.append(dict(**loc, keys=value))
                    elif not self.in_bibliography:
                        for key in self.keys(value, loc):
                            self.citations[key].append(loc)
                elif cmd in {'newcommand', 'renewcommand', 'providecommand',
                             'DeclareRobustCommand', 'def', 'gdef', 'edef', 'xdef'}:
                    # Macro definitions are not rendered prose. Ignore static
                    # definitions and fail if their bodies generate citations.
                    q = options(s, p)
                    if cmd in {'def', 'gdef', 'edef', 'xdef'}:
                        q = s.find('{', q)
                    else:
                        if q < len(s) and s[q] == '{':
                            _, q = group(s, q)
                        else:
                            target = re.match(r'\\[A-Za-z@]+', s[q:])
                            if not target:
                                raise ValueError('Unsupported command definition')
                            q += len(target.group())
                        q = options(s, q)
                    if q < 0:
                        raise ValueError('Unclosed command definition')
                    body, p = group(s, q)
                    if DYNAMIC_BODY.search(body):
                        raise ValueError('Citation/input-generating macro requires expanded-TeX audit')
                elif cmd in {'newenvironment', 'renewenvironment', 'provideenvironment'}:
                    _, q = group(s, options(s, p))
                    first, q = group(s, options(s, q))
                    last, p = group(s, q)
                    if DYNAMIC_BODY.search(first + '\n' + last):
                        raise ValueError('Citation/input-generating environment definition requires expanded-TeX audit')
                elif cmd in MULTICITES or cmd in {'bibliography', 'addbibresource', 'includeonly'} or cmd.startswith('if'):
                    raise ValueError('Unsupported construct requires TeX build audit: \\' + cmd)
            except ValueError as exc:
                self.error(loc, str(exc))
        # State may cross input boundaries intentionally.

    def result(self):
        missing = sorted(set(self.citations) - set(self.entries))
        uncited = sorted(set(self.entries) - set(self.citations))
        duplicate = {k:v for k,v in self.entries.items() if len(v) > 1}
        if not self.entries:
            self.errors.append({'message':'No explicit bibitem entries; cannot establish closure'})
        if self.in_bibliography:
            self.errors.append({'message':'Unclosed thebibliography environment'})
        ok = not (missing or uncited or duplicate or self.errors)
        return {'status':'PASS_CITATION_KEY_CLOSURE_ONLY' if ok else 'FAIL',
                'scope':'Direct citations and explicit bibitems only; no metadata or semantic verification',
                'files_sha256':self.files, 'citation_key_count':len(self.citations),
                'bibliography_entry_count':sum(map(len,self.entries.values())),
                'bibliography_environment_count':self.bibliography_count,
                'undefined_citations':{k:self.citations[k] for k in missing},
                'uncited_entries':{k:self.entries[k] for k in uncited},
                'duplicate_entries':duplicate, 'nocite_not_counted':self.nocites,
                'errors':self.errors, 'citation_locations':dict(self.citations)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tex', required=True, type=Path)
    parser.add_argument('--root', type=Path, help='Allowed local input root; default main file directory')
    parser.add_argument('--out', type=Path, help='Optional JSON report')
    args = parser.parse_args()
    check = Checker((args.root or args.tex.parent).resolve())
    check.read(args.tex)
    report = check.result()
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(rendered + '\n')
    print(rendered)
    return 0 if report['status'].startswith('PASS') else 1


if __name__ == '__main__':
    sys.exit(main())
