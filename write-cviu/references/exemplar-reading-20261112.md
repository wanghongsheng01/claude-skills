# Three CVIU exemplars: observation, use, and boundary

Reading verified on 2026-11-12. These are authoring observations, not journal requirements or explanations of acceptance. All three works have verified CVIU publication metadata. Two readings use explicitly versioned author manuscripts; one uses an institution-hosted, journal-formatted article. No third-party full text or original figure is redistributed here.

## VDGS: make the intervention and its visual object visible

**Gaussian Splatting with NeRF-based color and opacity**, CVIU 251 (2025), 104273, DOI [10.1016/j.cviu.2024.104273](https://www.sciencedirect.com/science/article/pii/S1077314224003540). The full reading is [author version v5](https://arxiv.org/html/2312.13729v5), not the final article.

- **Location and observation:** Fig. 1 pairs a full scene and its marked region with matched GT/method/baseline crops. Fig. 2 distinguishes operation and gradient flows. Section 4, Tables 5–6, separates operator choices from measured training and rendering costs. Section 5 concentrates the task boundary.
- **Transfer:** Let a figure expose the phenomenon measured by the claim. Draw actual inputs, modified parameters, and outputs; use a controlled alternative table to explain the chosen operation. Report costs from measurements under stated conditions.
- **Do not transfer:** Table numbers and experimental coverage changed in the final article. General speed adjectives should not substitute for the measured timing table. A method-specific appearance improvement does not establish a new allocation method's benefit.

## NeRFtrinsic Four: measure the intermediate claim separately

**NeRFtrinsic Four: An end-to-end trainable NeRF jointly optimizing diverse intrinsic and extrinsic camera parameters**, CVIU 249 (2024), 104206, DOI [10.1016/j.cviu.2024.104206](https://www.sciencedirect.com/science/article/pii/S107731422400287X). The full reading is [author version v4](https://arxiv.org/html/2303.09412v4).

- **Location and observation:** Section 4.2 separates image-quality and camera-parameter errors. Fig. 3 uses corresponding full images and local details. Section 4.6 tests specified design choices and reduced inputs; Section 5 discusses appearance scores coexisting with incorrect poses.
- **Transfer:** A claim about geometry, calibration, or a controller's decisions needs its own measurement. Place the perceptual example next to the quantitative comparison it illustrates. Organize related work by supervision and optimized variables.
- **Do not transfer:** An author-version limitation is not automatically a final-version limitation. The final publisher's visible Section 6 discusses a 360-degree integration requiring noisy-pose initialization. Do not copy its task-specific failure threshold or any best-run reporting as a general evaluation rule.

## Holistic triangulation: align each claim with its comparison

**View consistency aware holistic triangulation for 3D human pose estimation**, CVIU 236 (2023), 103830, DOI [10.1016/j.cviu.2023.103830](https://www.sciencedirect.com/science/article/abs/pii/S1077314223002102). The full nine-page [institution-hosted journal-formatted copy](https://cvl.sjtu.edu.cn/Upload/Paper/View%20Consistency%20Aware%20Holistic%20Triangulation%20for%203D%20Human%20Pose%20Estimation.pdf) was read.

- **Location and observation:** Fig. 1 (p. 2) gives the full pipeline; Fig. 2 (p. 3) contrasts the central operation with its baseline. Section 4.2 defines distinct accuracy and plausibility measurements. Table 3 (p. 6) displays input type, accuracy, and computation. Tables 5–8 (p. 7) address specific design choices. Section 4.5 ties limitations to the prior and view conditions; Fig. 6 (p. 8) marks the measured anatomical defects.
- **Transfer:** Use a compact comparison whose labels state what changes and what is held constant. Make qualitative annotations correspond to the claimed property. Concentrate boundary statements around an explicit failure mechanism and operating condition.
- **Do not transfer:** Pose-plausibility metrics do not measure rendering quality. Published captions still require consistency checks; this copy's Table 8 caption and three-view entries should not be treated as an error-free reporting template.

## Shared application rule

Choose an example because its evidence structure matches the present claim. Reuse the reasoning pattern, not its result, crop choice, fixed figure count, statistical threshold, or superiority language. Preserve contrary findings and distinguish an observed comparison from a causal explanation.
