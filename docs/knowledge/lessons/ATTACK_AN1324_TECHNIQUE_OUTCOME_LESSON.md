# AN1324 Analytic 1324 Outcome Lesson

## Authoritative description

- Technique: **AN1324 — Analytic 1324**
- Platforms: Windows

Detection of token duplication and impersonation attempts by correlating suspicious command-line executions (e.g., runas) with API calls to DuplicateToken, DuplicateTokenEx, ImpersonateLoggedOnUser, or SetThreadToken. The chain includes the initial command execution or in-memory API invocation → token handle duplication or thread token assignment → a new or existing process assuming the impersonated user's context.

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
- AN1324: https://attack.mitre.org/detectionstrategies/DET0482#AN1324
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
