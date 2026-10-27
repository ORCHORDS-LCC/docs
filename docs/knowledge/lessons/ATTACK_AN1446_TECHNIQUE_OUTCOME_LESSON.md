# AN1446 Analytic 1446 Outcome Lesson

## Authoritative description

- Technique: **AN1446 — Analytic 1446**
- Platforms: Windows

Monitors execution of administrative utilities (e.g., bcdedit.exe) or registry modifications that disable Driver Signature Enforcement (DSE) or enable Test Signing. Correlates command-line activity, registry changes, and subsequent process executions that bypass signing enforcement.

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
- AN1446: https://attack.mitre.org/detectionstrategies/DET0523#AN1446
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
