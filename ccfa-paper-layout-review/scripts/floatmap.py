#!/usr/bin/env python3
"""floatmap.py MAIN.tex : list every float (figure/table/algorithm, starred or not) in source order with
its placement spec, label, source file:line, and the source file:line of its first \\ref / \\cref, after
expanding \\input/\\include. Also lists \\FloatBarrier, \\clearpage, \\newpage and negative \\vspace with their
position, so a layout fixer can see which float definitions sit far after their first reference
(a typical cause of stranded floats and of the holes in front of a barrier). Read-only."""
import os, re, sys

def expand(path, out, seen):
    base = os.path.dirname(path)
    if path in seen or not os.path.exists(path):
        return
    seen.add(path)
    for i, line in enumerate(open(path, errors='ignore'), 1):
        code = re.sub(r'(?<!\\)%.*', '', line)
        m = re.search(r'\\(input|include)\{([^}]+)\}', code)
        if m:
            p = os.path.join(os.path.dirname(sys.argv[1]), m.group(2))
            if not p.endswith('.tex'):
                p += '.tex'
            if not os.path.exists(p):
                p2 = os.path.join(base, m.group(2)); p = p2 if os.path.exists(p2) else p2 + '.tex'
            before = code[:m.start()]
            if before.strip():
                out.append((path, i, before))
            expand(p, out, seen)
            rest = code[m.end():]
            if rest.strip():
                out.append((path, i, rest))
        else:
            out.append((path, i, code))

def main():
    main_tex = sys.argv[1]; root = os.path.dirname(os.path.abspath(main_tex))
    lines = []; expand(main_tex, lines, set())
    floats = []; cur = None; firstref = {}; events = []
    for idx, (f, i, code) in enumerate(lines):
        rel = os.path.relpath(f, root)
        for m in re.finditer(r'\\begin\{(figure|table|algorithm)(\*?)\}\s*(\[[^\]]*\])?', code):
            cur = dict(env=m.group(1) + m.group(2), spec=m.group(3) or '(default tbp)', at=f'{rel}:{i}', idx=idx, label=None)
            floats.append(cur)
        for m in re.finditer(r'\\label\{([^}]+)\}', code):
            if cur and cur['label'] is None:
                cur['label'] = m.group(1)
        if cur and re.search(r'\\end\{(figure|table|algorithm)\*?\}', code):
            cur = None
        for m in re.finditer(r'\\(?:[cC]ref|ref|autoref|Cref)\{([^}]+)\}', code):
            for lab in m.group(1).split(','):
                firstref.setdefault(lab.strip(), (f'{rel}:{i}', idx))
        for pat, name in [(r'\\FloatBarrier', 'FloatBarrier'), (r'\\clearpage', 'clearpage'), (r'\\newpage', 'newpage'),
                          (r'\\vspace\*?\{\s*-', 'negative vspace'), (r'\\balance\b', 'balance'), (r'\\enlargethispage', 'enlargethispage')]:
            if re.search(pat, code):
                events.append((idx, f'{rel}:{i}', name))
    print('| # | env | spec | label | defined at | first ref at | def - ref (source lines) |')
    print('|---|---|---|---|---|---|---|')
    for n, fl in enumerate(floats, 1):
        r = firstref.get(fl['label'] or '', None)
        d = fl['idx'] - r[1] if r else None
        print(f"| {n} | {fl['env']} | {fl['spec']} | {fl['label']} | {fl['at']} | {r[0] if r else 'NOT REFERENCED'} | {d if d is not None else '-'} |")
    if events:
        print('\nBarriers / page breaks / spacing hacks in source order:')
        for idx, at, name in events:
            print(f'- {at}: {name}')

if __name__ == '__main__':
    main()
