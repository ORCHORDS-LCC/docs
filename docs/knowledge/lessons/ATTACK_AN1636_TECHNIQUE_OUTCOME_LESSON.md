# AN1636 Analytic 1636 Outcome Lesson

## Authoritative description

- Technique: **AN1636 — Analytic 1636**
- Platforms: IaaS

Detects exploitation of IaaS cloud security boundaries to evade defense controls. Defender perspective includes anomalous API calls that bypass audit logging, disable monitoring, or manipulate guardrails (e.g., CloudTrail tampering). Correlation highlights when exploitation attempts precede sudden absence of expected telemetry.

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
- AN1636: https://attack.mitre.org/detectionstrategies/DET0595#AN1636
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
