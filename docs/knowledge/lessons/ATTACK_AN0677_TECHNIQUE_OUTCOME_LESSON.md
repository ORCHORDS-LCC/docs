# AN0677 Analytic 0677 Outcome Lesson

## Authoritative description

- Technique: **AN0677 — Analytic 0677**
- Platforms: Windows

Database client execution (e.g., sqlcmd.exe, isql.exe) by users or from locations not tied to enterprise automation or backups. Often followed by creation of .sql/.bak/.csv files, registry artifacts for ODBC/JDBC drivers, or encrypted ZIPs. Defender sees SQL tools launched by explorer.exe, Powershell, or odd parent processes, plus file writes in user temp locations.

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
- AN0677: https://attack.mitre.org/detectionstrategies/DET0242#AN0677
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
