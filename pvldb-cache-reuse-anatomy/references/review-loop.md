# Reviewer / fixer loop

Roles never mix in one round: the **reviewer** judges an exact version and writes fix requests; the **fixer** changes the
method, experiments or text and delivers a new exact version; a different reviewer pass (or a fresh reviewer) re-judges.

## Each round

1. **Lock the version**: PDF hash, source hash, artifact/DEV hashes, page count.
2. **Gate A** matrix (`gate-a-all-metrics.md`). Any FAIL/PARTIAL/MISSING row → an algorithm-level fix request.
3. **Gate B** walk (`section-anatomy.md`, `fingerprints.md`) → findings by impact: blocking / major / minor.
4. **Fix-request list**: `ID | gate | severity | location | exemplar evidence | required change | acceptance test`.
   Keep IDs stable across rounds; never silently drop a request.
5. **Deliver** to the fixer with the exact version hashes.

## Re-review of the next delivery

- Verify the new hashes and that frozen TEST/gold/scorer/headline numbers were not tuned after the freeze.
- For each open ID: CLOSED (acceptance test met on the new version, with evidence), OPEN, or REGRESSED.
- A Gate-A row closes only with new measured results; text changes never close it.
- Re-run the full Gate-A matrix — fixes can break other metrics.

## Approval

Approve only when every Gate-A row is PASS (or a tie proven at a floor) and no blocking/major Gate-B finding remains.
If either gate fails, issue the next minimal set of requirements; never lower the bar, never declare the paper abandoned.
