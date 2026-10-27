# AN1053 Analytic 1053 Outcome Lesson

## Authoritative description

- Technique: **AN1053 — Analytic 1053**
- Platforms: IaaS

Correlate creation or modification of serverless functions (e.g., AWS Lambda, GCP Cloud Functions, Azure Functions) with anomalous IAM role assignments or permissions escalation events. Detect subsequent executions of newly created functions that perform unexpected actions such as spawning outbound network connections, accessing sensitive resources, or creating additional credentials.

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
- AN1053: https://attack.mitre.org/detectionstrategies/DET0374#AN1053
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
