# Candidate and experiment plan

Use one card per materially different scientific question. Fill unknowns explicitly rather than inventing available assets or results.

|Field|Required substance|
|---|---|
|Identity|Candidate ID, revision, parent if reframed, search cutoff, planning decision|
|Problem|Inputs, outputs, training/test information, deployment condition, practical consequence|
|Evidence|Observed failure versus reported failure; exact source and reading depth|
|Closest work|Primary sources, mechanisms, assumptions, strongest threat to originality|
|Residual question|What remains unresolved within the declared search; what would close it|
|Proposed operation|Explicit computation or intervention and every added assumption/resource|
|Identifiability|Observationally indistinguishable cases and information needed to separate them|
|Hypotheses|Predicted direction, affected condition, endpoint and mechanism diagnostic|
|Falsifiers|Direct prior art, simple-control parity, absent natural-data failure, or resource-confounded gain|
|Assets|Data/version/license, code/commit/license, model/checkpoint, access and runnable status|
|Primary evaluation|Primary comparison, metric/scorer, independent unit and meaningful effect|
|Controls|Strong matched baseline, simple repair, information/compute-matched variants, oracle separately|
|Splits|Group unit, development selection, untouched confirmation, nuisance and object separation|
|Uncertainty|Training randomness, sampling uncertainty, paired structure and multiplicity|
|Cost|Draft run count, preprocessing/tuning/inference boundary, memory, time and external cost|
|Stopping|A result or missing prerequisite that stops scaling, not an arbitrary favorable score|
|Contribution boundary|What a positive result would justify; what it would still not prove|
|Next action|Concrete read-only clarification or smallest future decisive experiment|

For a sensor failure, add a recording sheet with synchronized raw channels, missing-value convention, exposure, gain, projection settings, timestamps, object/session IDs, downstream outputs and independent reference measurement. For an SNN comparison, add input encoding, temporal horizon, state reset policy, deadline, actual hardware and a matched non-spiking temporal control.

At the planning stage, list planned trials separately from executed trials. A design file is not a result table and is not a frozen execution protocol until datasets, code, scorer and all choices are fixed before outcome inspection.
