# AN0045 Analytic 0045 Outcome Lesson

## Authoritative description

- Technique: **AN0045 — Analytic 0045**
- Platforms: Windows

Detects unusual command executions and service modifications that indicate self-patching or disabling of vulnerable services post-compromise. Defenders should monitor for service stop commands, suspicious process termination, and execution of binaries or scripts aligned with known patching or service management tools outside of expected admin contexts.

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
- AN0045: https://attack.mitre.org/detectionstrategies/DET0015#AN0045
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
