---
name: "academic-latex-polish"
description: "Polish the English of a LaTeX research paper to the register of published CCF-A papers in its field (PVLDB/SIGMOD for data management; NeurIPS/ICML/ICLR for statistical ML and conformal methods) without changing any fact, number, macro, citation or reference."
---

# Academic LaTeX polish (PVLDB/SIGMOD register)

Use this skill when the user asks to polish, copy-edit or improve the readability of a LaTeX paper, especially a data-management or Text-to-SQL paper bound for PVLDB, SIGMOD, ICDE or an Elsevier/Springer journal. The rules come from studying published PVLDB papers (e.g., Jin et al., PVLDB 19; ParSEval, PVLDB 18).

## Workflow
0. **Study published papers of the same direction first.** Download the LaTeX sources of 4--6 published CCF-A papers that the manuscript cites or competes with (`curl -L https://arxiv.org/e-print/<id>`; untar each into its own folder). Measure their register with `scripts/style_stats.py` and compare with the manuscript; read their introductions and result paragraphs. Typical published values: mean sentence length 22--30 words, under 20% of sentences above 35 words, about 1 parenthesis and at most 0.3 semicolons per 100 words. Use the gap to decide what to fix.
1. **Snapshot first.** Copy `sections/`, `tables/` and `figs/` to a scratch folder before editing. That copy is the baseline for the preservation check.
2. **Ask the user what to leave alone.** Typical exclusions:
   - author-written declarations and AI-use statements;
   - front matter;
   - generated files (macro files such as `numbers*.tex`, and generated tables).

   Never edit those.
3. **Polish file by file.** For long papers, split the files among parallel workers, each with its own files. Give every worker the rules below and the checker.
4. **Check every file** with the preservation checker (below). It must print `OK`. Review each `[numbers, review]` line by hand.
5. **Scan punctuation** across all files:
   - no Unicode quotes `“ ” ‘ ’`;
   - no full-width punctuation `，。：；（）`;
   - no straight `"` used as quotation marks;
   - no `e.g.\ ` or `i.e.\ ` without a comma;
   - no parentheses in `\section`/`\subsection` titles;
   - British spellings converted to American (or the reverse, as the venue requires).
6. **Compile.** Check for undefined references and overfull boxes, render the pages with figures and tables, and read the key paragraphs (abstract, findings, the most edited section) for flow.
7. **Commit and push** in logical chunks, then report in the user's language which kinds of changes were made and which parts were left alone.

## Writing rules
1. **Preserve content exactly.**
   - Never change a claim, number, hedge, statistical result, hypothesis outcome, pre-registered/post hoc status, caveat or limitation.
   - Never add content.
   - Every `\V{...}`-style macro, `\ref`, `\cite`, `\label`, `\Tab`, math expression and environment must survive; it may move within the sentence.
2. **Structure.** Each paragraph opens with its point; the evidence follows. In the introduction, follow this order: context, problem, concrete example, gap in prior work, approach, headline findings, numbered contributions.
3. **Sentences.**
   - Aim for 15–30 words; split anything over about 35.
   - Use at most one semicolon per sentence, and avoid chains of the form "X; Y; Z".
   - Use explicit transitions: "However", "In contrast", "As a result", "To address this, we ...".
4. **Parentheses.**
   - At most one per sentence, never nested.
   - Keep them only for:
     - a compact statistic after its claim, e.g. `(95\,\% CI ...)` or `($p=...$)`;
     - an abbreviation at first use;
     - a short `e.g.,`/`i.e.,` list;
     - a pointer to a section, table or figure.
   - Turn other asides into a separate sentence or an appositive, or use "such as".
   - Move qualifiers such as "(post hoc)" or "(Stage 3)" out of headings into the first sentence of the section.
5. **Numbers.** State the claim first, then the count or share, as in "certifies 1,979 of the 7,995 pairs (24.8%)". Follow a statistic with a plain verdict, such as "the difference is significant".
   - Write ranges with negative bounds as "$-0.05$ to $0.12$", not with an en dash.
6. **Terms and quotes.**
   - Introduce new terms with `\emph{}`.
   - Use LaTeX English quotes ``like this'' only for genuine quotations or ironic use.
   - Keep defined terms and tool names exactly as defined.
7. **Punctuation.**
   - `--` for ranges, `---` (no spaces) for dashes.
   - `e.g.,` and `i.e.,` with a comma.
   - Consistent American spelling (labeled, behavior, summarize, judgment, modeling).
8. **Voice.** Use "we" for the authors' actions and the present tense for results.
9. **Code literals.** Inside `\texttt{}`, write single quotes as `\textquotesingle{}` so that SQL literals print upright in every font setup.

## Lessons from conformal/selective-prediction papers (NeurIPS/ICLR, e.g., Hierarchical Selective Classification, Conformal Alignment, Conformal Factuality, Conformal Risk Control)
1. **One idea per sentence.** Drafts often pack a claim, its reason and a caveat into one sentence joined by a colon and semicolons. Split them: claim. Reason ("because ..."). Caveat ("However, ...").
2. **Name the method as a sentence subject.** After the method is introduced, start sentences with it ("\hlcl{} scores ... It accepts ...") instead of chaining "and ..., and ...".
3. **Results paragraphs.** State the comparison in words first, then the numbers: "On X at $\alpha=0.05$, the method accepts A against B." Do not stack several results in one sentence separated by semicolons; give each dataset its own sentence.
4. **Parenthetical numbers in prose.** Convert "(effort 0.12 against 0.30)" into "Its effort is 0.12, against 0.30 for ...". Keep a parenthesis only for one compact statistic, such as a paired difference, after its claim.
5. **Definitions.** Replace "(a marginal FDR, mFDR)" by "known as the marginal FDR (mFDR)"; replace "(wrong accepted over accepted)" by an appositive "that is, the share of ...".
6. **Dataset descriptions.** A long sentence listing corpora with nested parentheses becomes an itemized list, one corpus per item.
7. **Captions.** Use full sentences ("Bold marks ...", "$^\dagger$ marks ...") instead of "Bold: ...; $\dagger$: ...", and avoid parentheses in captions except for panel pointers such as (left).
8. **Equations end with punctuation** that matches the sentence; a sentence never restarts in lower case after a display.
9. **Word limits.** Elsevier abstracts are often limited to 250 words; recount after splitting sentences, because splitting adds words.
10. **Leave alone** the declarations, CRediT, competing interests, funding and algorithm pseudocode, except for spelling consistency (e.g., licence -> license, labelled -> labeled when the paper uses American spelling).

## Preservation checker
Save this as `check_preserve.py` (outside the paper repository) and run it as `python3 check_preserve.py OLD.tex NEW.tex`.

```python
import re, sys
from collections import Counter

def tokens(s):
    s = re.sub(r'(?<!\\)%.*', '', s)
    prot = Counter()
    for pat in (r'\\V\{[^}]*\}', r'\\ref\{[^}]*\}', r'\\label\{[^}]*\}', r'\\Tab\{[^}]*\}', r'\\input\{[^}]*\}',
                r'\\eqref\{[^}]*\}', r'\\(?:begin|end)\{[^}]*\}'):
        prot.update(re.findall(pat, s))
    for m in re.findall(r'\\cite[pt]?\{([^}]*)\}', s):
        prot.update('cite:' + k.strip() for k in m.split(','))
    maths = Counter(re.sub(r'\s+', '', m) for m in re.findall(r'(?<!\\)\$([^$]+)\$', s))
    nums = Counter(re.findall(r'(?<![\w{\\])\d[\d,.]*\d|(?<![\w{\\])\d',
                              re.sub(r'\\V\{[^}]*\}|\\\w+\{[^}]*\}', '', s)))
    return prot, maths, nums

a, b = sys.argv[1:3]
pa, ma, na = tokens(open(a).read()); pb, mb, nb = tokens(open(b).read())
bad = False
for name, x, y in (('protected', pa, pb), ('math', ma, mb)):
    if x != y:
        bad = True; print(f'[{name}] missing:', dict(x - y), ' added:', dict(y - x))
if na != nb:
    print('[numbers, review] missing:', dict(na - nb), ' added:', dict(nb - na))
print('OK' if not bad else 'PROTECTED TOKENS CHANGED'); sys.exit(1 if bad else 0)
```

The checker treats added environments, added math such as an extra `$\alpha$`, and a number moved into a `\textbf{}` list label as changes. Inspect each reported difference: a new `itemize` for a dataset list or a repeated `$\alpha$` after splitting a sentence is acceptable; a missing `\res`/`\stat`/`\V` macro never is. Also count the paper's own number macros directly (e.g., `\res{...}{...}{...}{...}`, `\stat{...}`) before and after.

Adapt the macro pattern (`\\V\{...\}`) to the paper's own number macros if it uses a different name.