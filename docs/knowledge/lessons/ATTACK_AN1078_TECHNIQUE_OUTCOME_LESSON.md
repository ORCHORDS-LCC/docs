# AN1078 Analytic 1078 Outcome Lesson

## Authoritative description

- Technique: **AN1078 — Analytic 1078**
- Platforms: Linux

Detects creation or renaming of accounts with names that closely match known service, root, or admin accounts. Behavior often follows account discovery or deletion, attempting to blend into system activity logs using trusted name conventions.

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
- AN1078: https://attack.mitre.org/detectionstrategies/DET0383#AN1078
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
