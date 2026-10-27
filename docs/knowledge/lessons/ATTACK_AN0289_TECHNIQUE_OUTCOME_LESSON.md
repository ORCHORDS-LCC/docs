# AN0289 Analytic 0289 Outcome Lesson

## Authoritative description

- Technique: **AN0289 — Analytic 0289**
- Platforms: macOS

Detects unauthorized additions or changes to /Library/Security/SecurityAgentPlugins and suspicious process activity attempting to hook authentication APIs. Correlates file modifications with abnormal plugin loads in authentication flows.

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
- AN0289: https://attack.mitre.org/detectionstrategies/DET0104#AN0289
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
