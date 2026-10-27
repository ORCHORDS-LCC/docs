# AN0870 Analytic 0870 Outcome Lesson

## Authoritative description

- Technique: **AN0870 — Analytic 0870**
- Platforms: macOS

Detection of fake or spoofed macOS Security & Privacy GUIs showing healthy status after XProtect, Gatekeeper, or AV processes are disabled. Correlates user-space UI process creation with terminated or missing security daemons.

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
- AN0870: https://attack.mitre.org/detectionstrategies/DET0311#AN0870
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
