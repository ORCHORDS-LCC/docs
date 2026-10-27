# AN1178 Analytic 1178 Outcome Lesson

## Authoritative description

- Technique: **AN1178 — Analytic 1178**
- Platforms: Windows

Correlate DNS queries that generate domains with high entropy or gibberish patterns, combined with short-lived connections from unusual processes. Monitor Sysmon DNS events and Windows Security logs for abnormal query rates and failed lookups.

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
- AN1178: https://attack.mitre.org/detectionstrategies/DET0419#AN1178
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
