# AN1211 Analytic 1211 Outcome Lesson

## Authoritative description

- Technique: **AN1211 — Analytic 1211**
- Platforms: Windows

Modification or replacement of service executables due to weak file or directory permissions. Defender observes file writes to service binary paths, unexpected modifications of executables associated with registered services, and subsequent service execution of attacker-supplied binaries under elevated permissions.

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
- AN1211: https://attack.mitre.org/detectionstrategies/DET0436#AN1211
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
