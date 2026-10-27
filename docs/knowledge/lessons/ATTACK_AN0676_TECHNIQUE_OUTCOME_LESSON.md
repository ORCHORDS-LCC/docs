# AN0676 Analytic 0676 Outcome Lesson

## Authoritative description

- Technique: **AN0676 — Analytic 0676**
- Platforms: Linux

Unusual database command-line access (e.g., `psql`, `mysql`, `mongo`) from non-admin users, occurring outside typical automation windows or without known service context. Often followed by data dumps to .sql/.csv files or outbound data transfers. Defender sees CLI tools launched interactively or by unusual parent processes, file writes to dump-like filenames, and external connections shortly after.

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
- AN0676: https://attack.mitre.org/detectionstrategies/DET0242#AN0676
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
