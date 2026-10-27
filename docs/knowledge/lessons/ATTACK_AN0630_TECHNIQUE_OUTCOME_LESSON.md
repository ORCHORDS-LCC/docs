# AN0630 Analytic 0630 Outcome Lesson

## Authoritative description

- Technique: **AN0630 — Analytic 0630**
- Platforms: Windows

Detects behavior where files with non-executable or misleading extensions (e.g., .jpg, .txt) are created or modified but subsequently executed as binaries based on internal file headers or abnormal parent process lineage. This includes identifying polyglot files or malformed magic bytes indicative of masquerading attempts.

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
- AN0630: https://attack.mitre.org/detectionstrategies/DET0226#AN0630
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
