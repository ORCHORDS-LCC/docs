# AN1480 Analytic 1480 Outcome Lesson

## Authoritative description

- Technique: **AN1480 — Analytic 1480**
- Platforms: Windows

1) New or updated software is delivered/installed from atypical sources or with signature/hash mismatches; 2) installer/updater writes binaries to unexpected paths or replaces existing signed files; 3) first run causes unsigned/abnormally signed modules to load or child processes to execute, optionally followed by network egress to new destinations.

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
- AN1480: https://attack.mitre.org/detectionstrategies/DET0537#AN1480
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
