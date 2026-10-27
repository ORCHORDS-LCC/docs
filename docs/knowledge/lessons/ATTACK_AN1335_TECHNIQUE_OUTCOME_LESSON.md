# AN1335 Analytic 1335 Outcome Lesson

## Authoritative description

- Technique: **AN1335 — Analytic 1335**
- Platforms: Windows

Identifies abuse of odbcconf.exe to execute malicious DLLs using the REGSVR command flag. Behavior chain: (1) Process creation of odbcconf.exe with /REGSVR or /A {REGSVR ...} arguments → (2) DLL load by odbcconf.exe of non-standard or unsigned modules → (3) Optional follow-on process creation or network activity from loaded DLL.

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
- AN1335: https://attack.mitre.org/detectionstrategies/DET0486#AN1335
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
