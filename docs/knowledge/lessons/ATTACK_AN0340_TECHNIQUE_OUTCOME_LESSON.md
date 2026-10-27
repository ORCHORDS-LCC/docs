# AN0340 Analytic 0340 Outcome Lesson

## Authoritative description

- Technique: **AN0340 — Analytic 0340**
- Platforms: macOS

Creation or modification of Login Items using AppleScript or Service Management Framework. Detection focuses on file creation/modification of `backgrounditems.btm`, new executables in `Contents/Library/LoginItems/`, use of `SMLoginItemSetEnabled` API, or suspicious processes triggered post-login without user interaction. Behavioral pivot includes anomalous AppleEvents, suspicious parent-child process pairs, and login-triggered execution chains.

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
- AN0340: https://attack.mitre.org/detectionstrategies/DET0121#AN0340
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
