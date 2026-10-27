# AN2029 Analytic 2029 Outcome Lesson

## Authoritative description

- Technique: **AN2029 — Analytic 2029**
- Platforms: Windows

Process execution without GUI context (e.g., powershell.exe, wscript.exe) generates HTTP traffic with a spoofed User-Agent mimicking a legitimate browser. No corresponding UI application (e.g., msedge.exe) is active or in parent lineage. The User-Agent deviates from known enterprise baselines or contains spoofed platform indicators. User-Agent strings can be gathered with API calls such as `ShellExecuteW` to open the default browser on a socket to receive an HTTP reply, or by hard coding the User-Agent string for a specific browser.

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
- AN2029: https://attack.mitre.org/detectionstrategies/DET0898#AN2029
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
