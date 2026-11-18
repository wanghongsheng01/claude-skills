# ProRP: proactive resource provisioning

## Source and reading scope
- SIGMOD 2024 formal publication, DOI: https://doi.org/10.1145/3626246.3653371
- Author-hosted publication PDF: https://www.microsoft.com/en-us/research/uploads/prod/2024/03/prorp.pdf
- Checked 2026-11-18: publication-text and section/figure-structure reading; not sentence-level rhetorical annotation or an independent reproduction.
- Observed: 14 pages, 12 figures, 1 table, 5 algorithms, 68 references. Counts are descriptive, not quotas.

## Observed structure and evidence
Sections 1–2 establish the problem and conflicting objectives; 3–8 cover principles, policy, recording, prediction, wake-up, telemetry and training. Section 9 evaluates, 10 relates prior work, 11 states boundaries.

Across four Azure regions, comparison with reactive provisioning reports login resource readiness moving from approximately 60–68% to 80–90%, idle resources from 5–12% to 7–14%, and roughly doubled operations. These ranges describe the reported settings, not universal gains. The control is binary on/off; releasing a resource is not automatically a billing saving.

## Interpretation and proposed transfer
A stronger service outcome can justify an explicit resource and operations tradeoff. For another industrial controller, map requirements to policies and telemetry, then measure quality, idle capacity and intervention cost together. Distinguish measured deployment outcomes from potential savings. Specify the actuator's scope and compare against the actual operational alternative. These are review questions inferred from this example, not SIGMOD requirements or proof that the candidate is deployable.
