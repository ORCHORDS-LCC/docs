# AN1288 Analytic 1288 Outcome Lesson

## Authoritative description

- Technique: **AN1288 — Analytic 1288**
- Platforms: Windows

Execution of Microsoft-signed scripts (e.g., pubprn.vbs, installutil.exe, wscript.exe, cscript.exe) used to proxy execution of untrusted or external binaries. Behavior is detected through command-line process lineage, child process spawning, and unsigned payload execution from signed parent.

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
- AN1288: https://attack.mitre.org/detectionstrategies/DET0466#AN1288
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
