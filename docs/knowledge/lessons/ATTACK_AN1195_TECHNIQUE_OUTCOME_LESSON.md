# AN1195 Analytic 1195 Outcome Lesson

## Authoritative description

- Technique: **AN1195 — Analytic 1195**
- Platforms: Windows

Unauthorized modification of service-related registry keys such as ImagePath, FailureCommand, ServiceDll, or Performance/Parameters keys. Defender correlates registry modifications, anomalous service metadata changes, and subsequent service process executions that deviate from baseline configurations.

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
- AN1195: https://attack.mitre.org/detectionstrategies/DET0427#AN1195
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
