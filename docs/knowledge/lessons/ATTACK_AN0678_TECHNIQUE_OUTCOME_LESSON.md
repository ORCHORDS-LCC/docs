# AN0678 Analytic 0678 Outcome Lesson

## Authoritative description

- Technique: **AN0678 — Analytic 0678**
- Platforms: macOS

Execution of Java-based or CLI database tools (e.g., DBeaver, Beekeeper, mysql, psql) from user profiles not tied to dev/admin roles, especially when followed by file writes and cloud sync activity. Defender correlates GUI tool launches, file write events in ~/Downloads or ~/Documents, and outbound API calls to known cloud services.

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
- AN0678: https://attack.mitre.org/detectionstrategies/DET0242#AN0678
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
