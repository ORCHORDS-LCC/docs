# AN0871 Analytic 0871 Outcome Lesson

## Authoritative description

- Technique: **AN0871 — Analytic 0871**
- Platforms: Windows

Multi-event correlation of Registry creation under Active Setup with anomalous execution of processes at user logon. Behavioral patterns include creation/modification of HKLM Active Setup keys with non-standard StubPath values, followed by process execution from uncommon paths, unsigned binaries, or unusual parent-child lineage post-user login.

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
- AN0871: https://attack.mitre.org/detectionstrategies/DET0312#AN0871
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
