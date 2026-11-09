---
name: pr-evidence-reading
description: Deep-read formally published Pattern Recognition papers by scientific problem, extracting their key mechanism, experimental evidence and writing structure with page/table anchors.
---

# Pattern Recognition evidence reading

Read published papers to learn their scientific reasoning, not to infer why a confidential editorial decision occurred. This skill produces critical full-text reading notes, not new research ideas or claimed reproductions.

For concrete examples from the ten-paper study, read [published learning cases](references/published-lessons.md). Each example names the actual reading version and the evidence location; adapt the lesson to the new paper instead of copying its protocol.

## Establish what was actually read

Record DOI, journal year/volume, publisher publication evidence, full-text URL, version, hash and access date. A verified author manuscript may support reading but can differ from the journal version; say which. Abstract-only entries remain retrieval notes. Do not fill inaccessible sections from memory.

Read tables, figure captions, experimental protocol and limitations before adopting the abstract's narrative. Inspect rendered pages when equations, tables, diagrams or OCR are ambiguous. Distinguish author claims, paper-reported evidence, independently recomputed evidence and your interpretation.

## Scientific problem → mechanism → evidence

For each paper, record:

1. Inputs, outputs, supervision available at training/test, deployment shift and target failure. State the problem in terms that could be falsified, rather than paraphrasing the title.
2. The strongest alternative methods and their assumptions. Explain which assumption the paper relaxes and what new assumption or resource it introduces.
3. The mechanism in equations or explicit operations: what quantity is computed, what constraint/loss is added, where gradients or information flow, and why this is meant to fix the stated failure. Distinguish the key change from supporting architecture.
4. Datasets, split/grouping unit, leakage controls, preprocessing, backbone, external pretraining, label budget, tuning, seeds, metrics and uncertainty. Mark unreported fields as unreported.
5. Which table supports the main effect, which ablation isolates the mechanism, which experiment tests generality, and which measures compute or inference cost. Separate copied benchmark numbers from rerun baselines.
6. Failure distribution, assumptions and missing decisive tests. A better average metric does not prove lower variance, lower cost or universal superiority.

Every quantitative claim and critique needs a section/table/figure/page anchor. Check formula signs and monotonicity against verbal explanations; check improvements using the same metric and denominator. Do not declare a mechanism validated by publication alone.

## Learn writing in context

Map paragraph functions: practical failure → existing assumption → demonstrated gap → mechanism → evidence → scope. Explain how related work sets up the comparison, how the method introduces symbols, and how experiments answer claims in order. Record the actual order of main tables, mechanisms, ablations, efficiency and failures. Distinguish observed author practice from an official requirement.

Learn figure roles: a problem illustration, an architecture/operation diagram, evidence plots and failure examples serve different arguments. Record axes, units, aggregation, sample selection and uncertainty. Do not copy a decorative architecture merely because the paper was published.

## Cross-paper output

Group by **scientific problem first**, then compare mechanism families, evidence designs and writing strategies. Include a matrix of shared assumptions, genuinely differing mechanisms, resource fairness and unresolved limits. Explain transferable lessons and practices to avoid. Use a formal-paper/example bibliography with primary URLs. State that paper-reported results have not been reproduced unless a separate run log proves otherwise.
