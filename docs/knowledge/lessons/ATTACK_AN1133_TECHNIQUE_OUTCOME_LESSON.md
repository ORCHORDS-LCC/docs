# AN1133 Analytic 1133 Outcome Lesson

## Authoritative description

- Technique: **AN1133 — Analytic 1133**
- Platforms: Windows

Monitor Windows Registry modifications to Winlogon keys (Shell, Userinit, Notify) that introduce new executable or DLL paths. Correlate these changes with subsequent DLL loading, image loads, or process creation originating from winlogon.exe or userinit.exe. Abnormal child process lineage or unauthorized binaries in C:\Windows\System32 may indicate abuse.

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
- AN1133: https://attack.mitre.org/detectionstrategies/DET0404#AN1133
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
