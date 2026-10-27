# AN1112 Analytic 1112 Outcome Lesson

## Authoritative description

- Technique: **AN1112 — Analytic 1112**
- Platforms: macOS

Detects suspicious access to macOS Keychain files and APIs. Observes processes invoking the 'security' utility or accessing Keychain databases directly, correlates these with abnormal parent process lineage or unexpected user context. Monitors attempts to dump, unlock, or read credential storage beyond normal application workflows.

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
- AN1112: https://attack.mitre.org/detectionstrategies/DET0396#AN1112
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
