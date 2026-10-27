# AN0435 Analytic 0435 Outcome Lesson

## Authoritative description

- Technique: **AN0435 — Analytic 0435**
- Platforms: macOS

Detection focuses on adversaries placing or modifying malicious dylibs in locations searched by legitimate applications. From the defender’s perspective, observable patterns include unexpected creation or modification of dylib files in application bundle paths, unusual module loads by processes compared to historical baselines, and execution of applications loading dylibs from suspicious directories (e.g., /tmp, user-controlled paths). Correlation across file system changes, process execution, and module loads provides high-fidelity detection.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN0435: https://attack.mitre.org/detectionstrategies/DET0152#AN0435
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
