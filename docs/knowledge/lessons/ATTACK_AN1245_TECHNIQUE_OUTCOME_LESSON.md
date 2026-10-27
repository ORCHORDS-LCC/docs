# AN1245 Analytic 1245 Outcome Lesson

## Authoritative description

- Technique: **AN1245 — Analytic 1245**
- Platforms: Windows

Defenders can identify PowerShell profile-based persistence by correlating file creation or modification in known profile locations with subsequent PowerShell process launches that do not use the `-NoProfile` flag. Profile scripts loading unusual modules or launching external programs, particularly under elevated contexts, are suspicious and may represent adversary persistence or privilege escalation.

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
- AN1245: https://attack.mitre.org/detectionstrategies/DET0451#AN1245
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
