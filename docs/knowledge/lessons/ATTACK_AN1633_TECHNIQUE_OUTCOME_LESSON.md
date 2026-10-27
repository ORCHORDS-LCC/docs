# AN1633 Analytic 1633 Outcome Lesson

## Authoritative description

- Technique: **AN1633 — Analytic 1633**
- Platforms: Windows

Detects exploitation attempts targeting defensive security software or OS services. Defender observation includes abnormal process behavior (e.g., AV or EDR crashing unexpectedly), unsigned/untrusted modules loaded into defensive processes, or privilege escalation from security agent services. Multi-event correlation ties exploitation attempts to subsequent evasive behavior like service termination or missing logs.

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
- AN1633: https://attack.mitre.org/detectionstrategies/DET0595#AN1633
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
