# AN0074 Analytic 0074 Outcome Lesson

## Authoritative description

- Technique: **AN0074 — Analytic 0074**
- Platforms: Windows

Correlated registry modifications under Print Processors path, followed by DLL file creation within the system print processor directory, and DLL load by spoolsv.exe. Malicious execution often occurs during service restart or system boot, with SYSTEM-level privileges.

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
- AN0074: https://attack.mitre.org/detectionstrategies/DET0026#AN0074
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
