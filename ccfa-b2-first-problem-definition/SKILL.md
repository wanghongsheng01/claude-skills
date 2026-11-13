---
name: ccfa-b2-first-problem-definition
description: >-
  Use when a CCF-A paper's primary claim is that the scientific problem itself
  is first proposed and defined here (B2): how to abstract a production
  phenomenon into a researchable problem, prove it is not a renamed existing
  task, formalise input/output and evaluation, and write precise value for
  practice and for research. Do not use if a nearest neighbour already defines
  an equivalent problem (reclassify as B1), and do not use to justify skipping
  strong baselines or a careful evaluation.
---

# First defining a scientific problem (B2)

Official venue guidelines take precedence. This draft expands `skills-drafts/enterprise-need-to-formalized-problem/SKILL.md`. A B2 paper is not excused from rigorous experiments; its **first** job is a definition a reviewer will accept, with evidence of importance, generality, evaluability, and a clean increment over the closest named neighbour.

## When to use / when not

**Use** after front-loaded research has provisionally classified the paper as B2, and when writing the problem formalisation, the value argument, or the opening of the manuscript.

**Do not use**, and **reclassify as B1**, if a published neighbour already defines an equivalent input/output/constraint triple under another name. Do not use this skill to avoid comparing with strong methods once the problem is defined. A short demonstration paper that touches a similar object still counts as a neighbour; say that it is a demonstration and still write a falsifiable increment (see the ATLAS lesson in the existing enterprise-need note).

## Inputs and outputs

**In:** a production or social phenomenon (operators' words, not a marketing summary); a candidate formalisation; a neighbour table from official PDFs.

**Out:** an abstraction chain (phenomenon → observable contradiction → variables and constraints → scientific problem); a formal input/output/non-goal page; evidence of importance, generality, researchability, and evaluability; value statements that are precise for practice and for research; a baseline and concept-verification plan.

## Process — the abstraction chain

1. **Record the phenomenon in operators' words.** What they actually do next, including steps they admit cannot be fully automatic.
2. **Name a contradiction that can be observed** (a revocation that the cache serves stale; a prompt history that accumulates implicit quality rules; an ELT pipeline that is judged only by isolated subtasks).
3. **Turn the contradiction into variables and constraints** (input artefacts, output object, events, what is out of scope).
4. **Write a scientific problem** a database reviewer can restate without any vendor name. Mark non-claims.
5. **Prove it is not a rename.** Fill a neighbour table: venue and paper type; input; output; change trigger; verification; metric. One falsifiable increment sentence.
6. **Show why it is worth being a problem at this venue now:** a measure, a case, or a counterfactual (if defined wrongly, what breaks); preferably on public data.
7. **Give an evaluation that could refute the definition:** a baseline that should fail if the definition is right (for example, a neighbour's detector that is blind to a mutation you pre-register), and a concept verification that is not just a demo screenshot.
8. **Write value and boundary:** what changes for operators; what changes for other researchers (a new object, a new test, a new invariant). Do not promise a whole enterprise architecture. Do not write a partner's product as "our contribution".

## Evidence standard

Official PVLDB PDFs, 2026-11-12, vldb.org. Several papers below are **also** benchmark or method papers; they are used here because they **introduce a new object, class, or evaluation setting** and show how that introduction is argued. They are not all "pure B2 method papers". Where a paper is short (for example an 8-page constraints paper), that length is stated.

## Papers read this round (five)

### 1. SPADE — production phenomenon to a formal object

- Shreya Shankar, Haotian Li, Parth Asawa, Madelon Hulsebos, Yiming Lin, J.D. Zamfirescu-Pereira, Harrison Chase, Will Fu-Hinthorn, Aditya G. Parameswaran, Eugene Wu. *spade: Synthesizing Data Quality Assertions for Large Language Model Pipelines.* PVLDB, 17(12): 4173–4186, 2024. doi:[10.14778/3685800.3685835](https://doi.org/10.14778/3685800.3685835). Official PDF: https://www.vldb.org/pvldb/vol17/p4173-shankar.pdf
- **Abstraction chain:** developers already debug LLM pipelines by editing prompts over time (the phenomenon). Those edits encode implicit quality criteria, but they are not deployed as checks. The contradiction: errors are acknowledged as inevitable, yet the quality rules stay trapped in prompt history. The scientific object: automatically synthesise a **minimal set of assertion functions** from prompt-version histories, under coverage and accuracy constraints. Evaluation on nine real pipelines; abstract: 14% fewer assertions and 21% fewer false failures than simpler baselines. Deployment in LangSmith on over 2,000 pipelines is used as **importance evidence**, not as the scientific claim.
- **Thinking to reuse:** start from what practitioners already do; make that residue (prompt diffs) the input; define a precise output (assertions, not "better prompts"); evaluate against simple baselines on the same object; use deployment as value, not as a substitute for the experiment.
- **Boundary:** this is closer to "a new object on LLM pipelines" than to "the first definition of data quality". The paper does not pretend assertions are a new idea; it pretends—correctly—that **synthesising them from prompt histories** is the unformulated task. That is the right grain for a B2 increment.

### 2. Semantic Integrity Constraints — a declarative abstraction, honestly short

- Alexander W. Lee, Justin Chan, Michael Fu, Nicolas Kim, Akshay Mehta, Deepti Raghavan, Uğur Çetintemel. *Semantic Integrity Constraints: Declarative Guardrails for AI-Augmented Data Processing Systems.* PVLDB, 18(11): 4073–4080, 2025. doi:[10.14778/3749646.3749677](https://doi.org/10.14778/3749646.3749677). Official PDF: https://www.vldb.org/pvldb/vol18/p4073-lee.pdf. **Eight pages** (4073–4080): treat it as a short / vision-length formal paper, not a 12-page empirical study.
- **Abstraction chain:** AI-augmented data processing systems inherit LLM unreliability (hallucinations) that blocks adoption in high-stakes settings. Existing remedies (imperative assertions, constrained decoding) are "imperative and fragmented". The proposed object: **semantic integrity constraints (SICs)** as a declarative, unified abstraction that extends classical database integrity constraints from "invalid writes to the database" to "erroneous outputs of semantic operators".
- **Thinking to reuse:** they position the new object as an extension of a concept the venue already trusts (integrity constraints), which is a strong B2 persuasion strategy. They explicitly compare to SPADE-style assertions and to constrained decoding, so "first" is scoped. Because the paper is short, it shows how to argue a definition and a research agenda; a 12-page B2 research submission would still need the evaluation framework this paper only outlines.
- **Do not copy:** treating an 8-page formalisation as if it had a full empirical gate; if we cite it, state the length and paper type.

### 3. SemBench — naming a class, then evaluating it

- Jiale Lao et al. *SemBench: A Benchmark for Semantic Query Processing Engines.* PVLDB, 19(8): 1754–1767, 2026. doi:[10.14778/3811243.3811249](https://doi.org/10.14778/3811243.3811249). Official PDF: https://www.vldb.org/pvldb/vol19/p1754-trummer.pdf (full author list in the B1-benchmark skill).
- **Abstraction chain:** a "novel class of systems" (semantic query processing engines) is asserted from academic and industrial adoption, then given an operational definition (SQL extended with LLM-evaluated semantic operators on multi-modal data). The paper is a benchmark, but the opening is a B2-style **class definition**. Coverage is argued by axes (scenarios, modalities, operators), which is how to show a new class is researchable and evaluable.
- **Thinking to reuse:** if we claim a new class or a new problem, give an operational test for membership ("is this engine an SQPE?") and an evaluation that several systems can enter. A class name without a membership test looks like a rename.
- **Used also in the B1-benchmark skill**; here the lesson is the class-definition opening, not the item design.

### 4. TACO — a new evaluation setting justified by exclusion from existing benches

- Chao Deng, Ju Fan et al. *TACO: A Benchmark for Open-Domain Text-to-SQL with Ambiguous and Cross-Database Queries.* PVLDB, 19(6): 1386–1399, 2026. doi:[10.14778/3797919.3797942](https://doi.org/10.14778/3797919.3797942). Official PDF: https://www.vldb.org/pvldb/vol19/p1386-fan.pdf
- **Abstraction chain:** Text-to-SQL is old; the **setting** (open-domain, ambiguous, cross-database, unspecified schema) is what existing benches "fall short in addressing". The problem formulation section precedes the collection. Real smart-city data plus a stated synthesis pipeline addresses "is this real?" and "is this large enough?". A baseline exists to show the setting is hard, and the abstract refuses to declare the problem solved.
- **Thinking to reuse:** a B2-flavoured evaluation problem is justified by a **comparison table of settings**, not by a new buzzword. If our "first definition" is actually a new setting of an old problem, say that and consider B1-benchmark as the honest type, with this paper as the model.

### 5. ELT-Bench — a new end-to-end task because isolated tasks hide the difficulty

- Tengjun Jin, Yuxuan Zhu, Daniel Kang. *ELT-Bench: An End-to-End Benchmark for Evaluating AI Agents on ELT Pipelines.* PVLDB, 19(2): 84–98, 2025. doi:[10.14778/3773749.3773750](https://doi.org/10.14778/3773749.3773750). Official PDF: https://www.vldb.org/pvldb/vol19/p84-jin.pdf
- **Abstraction chain:** practitioners already build ELT pipelines by hand; AI methods look strong on isolated data tasks (including Text-to-SQL). The contradiction: there is no end-to-end evaluation of agents that must use tools, write SQL, and orchestrate every stage. The object: 100 full pipelines (835 source tables, 203 models). The result that "the highest-performing agent correctly generates only 11.3% of data models" (abstract), with cost and steps, is both evaluability evidence and importance evidence: the problem is not already solved by "LLMs are good at SQL".
- **Thinking to reuse:** if a sceptical reviewer says "this is just Text-to-SQL", the answer is a **task that existing strong agents fail at**, with a public protocol. Low scores of strong systems support a new problem; they are not a reason to weaken the baseline.
- **Also a B1-benchmark paper.** Use it in B2 only for the "why this is a distinct task" argument.

## Transferable persuasion habits

- **Grain of "first":** first to synthesise assertions from prompt histories (SPADE), first to treat SICs as a declarative integrity abstraction (SIC), first to evaluate a named system class (SemBench), first to evaluate a setting or an end-to-end task (TACO, ELT-Bench). Never "first to think about quality / SQL / ELT".
- **Extend a concept the venue already trusts** (integrity constraints → SICs) rather than inventing an isolated vocabulary.
- **Importance:** deployment numbers (SPADE), high-stakes adoption barriers (SIC), strong agents' low absolute scores (ELT-Bench).
- **Evaluability:** membership tests, public pipelines, axes of coverage, mutations a neighbour cannot see.
- **Value writing:** what operators can deploy (assertions, constraints); what researchers can now measure (a class, a setting). No product reconstruction.
- **Honesty about paper type and length** (SIC is 8 pages). A demonstration neighbour still requires a written increment.

## Checklists and gates

- [ ] Abstraction chain written; no vendor name in the problem sentence.
- [ ] Neighbour table from official PDFs; increment in one falsifiable sentence.
- [ ] If a neighbour is equivalent, reclassify to B1; do not keep B2.
- [ ] Importance, generality, researchability, evaluability each have evidence, or are marked insufficient.
- [ ] Evaluation could refute the definition (a mutation, a membership test, a strong agent that should fail or succeed for a stated reason).
- [ ] Value for practice and for research is specific; non-goals are explicit.
- [ ] Main-table claims stand on public or fully synthetic released data.

**Failure:** if reading shows an equivalent formalisation, stop and reclassify. If the only evidence of importance is an internal enterprise anecdote, that is insufficient for a CCF-A B2 claim until a public or de-identified measurable counterpart exists.

## Version

- 0.1 (2026-11-12, America/Los_Angeles): expands `enterprise-need-to-formalized-problem/SKILL.md` with five official PVLDB papers, each used for the definition-and-persuasion lesson stated above. To be expanded to 15–25, including ICDE and SIGMOD papers that first formalise an industrial problem as a database question. This version has not yet been used to start a new B2 paper from a blank page; it informed the type decision and gap list for paper 17 (Etl2BizSem) in the same round.
