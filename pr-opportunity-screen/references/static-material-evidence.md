# Static materials before scientific attribution

Use this when an application failure comes with source code, device manuals or exported logs. A static audit helps identify observable variables and competing explanations; it does not establish the cause of a recorded field failure.

Record each capability separately: source/version/hash, exact page or function/line, device or software applicability, documented support, implementation path, field activation, acquired sample, verification performed, and remaining unknowns. Do not collapse these into one “available” flag.

- Verify the exact device model and SDK owner. A robot API can expose execution state while offering no sensor frames. A generic software screenshot may illustrate a different sensor from the one deployed.
- Inspect complete PDF pages and footnotes for decisive specifications. Text extraction may miss screenshot labels or include hidden overlapping specifications. Treat a product's best-case latency, accuracy or lighting rating as a conditional vendor claim until measured in the target setup.
- Trace capture, preprocessing, recognition, pose, planning, transport and execution separately. State which segments are outside the inspected code. A command named capture or grasp does not expose every preceding stage.
- Read return-value semantics and their consumers. A success enum may mean the procedure completed or a queue ended; it does not necessarily mean an object was recognized or grasped. Do not infer a published metric counter without its actual update path.
- Inspect request/response identity, required payload fields, empty/malformed results, stale state and retry behavior. Separate certain branch behavior from possible asynchronous interleavings, and both from deployment evidence. These may be engineering explanations that must be controlled before claiming a novel perception failure.
- A logging library is not a field log; a save button is not a saved dataset. Distinguish raw and processed depth, missing and biased values, acquisition/receive/write clocks, coordinate registration and any extra hardware or frames used.
- Preserve the field failure as unresolved if only code and manuals are available. Plan the smallest passive evidence collection or offline replay that distinguishes explanations. Do not run equipment, alter live controls, invoke model APIs or fabricate sensor data as part of a planning-only request.

For paper decisions, keep two outcomes separate: an engineering defect may deserve repair but not a paper; a scientific hypothesis remains conditional until it survives that simpler explanation and the closest published method.
