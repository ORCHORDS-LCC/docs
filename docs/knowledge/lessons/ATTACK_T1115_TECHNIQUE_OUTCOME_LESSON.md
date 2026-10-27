# T1115 Clipboard Data Outcome Lesson

## Authoritative description

- Technique: **T1115 — Clipboard Data**
- Tactics: collection
- Platforms: Linux, macOS, Windows

Adversaries may collect data stored in the clipboard from users copying information within or between applications. For example, on Windows adversaries can access clipboard data by using clip.exe or Get-Clipboard. Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., Transmitted Data Manipulation). macOS and Linux also have commands, such as pbpaste, to grab clipboard contents.

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
- T1115: https://attack.mitre.org/techniques/T1115
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
