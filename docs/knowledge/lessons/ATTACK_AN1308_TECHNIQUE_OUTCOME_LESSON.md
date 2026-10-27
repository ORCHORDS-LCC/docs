# AN1308 Analytic 1308 Outcome Lesson

## Authoritative description

- Technique: **AN1308 — Analytic 1308**
- Platforms: Windows

Detects rundll32.exe invoked with atypical arguments (.dll, .cpl, javascript:, mshtml). DLLs not normally loaded by rundll32 are mapped into memory. Control_RunDLL or RunHTMLApplication invoked. Suspicious DLLs or scripts accessed from disk or network. Rundll32 reaches out to external domains (e.g., fetching .sct or .hta).

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
- AN1308: https://attack.mitre.org/detectionstrategies/DET0475#AN1308
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
