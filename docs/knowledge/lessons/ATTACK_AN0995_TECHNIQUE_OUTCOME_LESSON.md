# AN0995 Analytic 0995 Outcome Lesson

## Authoritative description

- Technique: **AN0995 — Analytic 0995**
- Platforms: Windows

Detection of processes launching downgraded PowerShell versions (e.g., v2) or other legacy binaries that lack logging or security features. Correlates command-line arguments, process metadata, and version fields. Monitors registry changes to Defender or HVCI keys that could indicate intentional downgrades.

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
- AN0995: https://attack.mitre.org/detectionstrategies/DET0350#AN0995
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
