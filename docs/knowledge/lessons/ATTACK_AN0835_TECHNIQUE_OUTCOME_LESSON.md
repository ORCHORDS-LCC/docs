# AN0835 Analytic 0835 Outcome Lesson

## Authoritative description

- Technique: **AN0835 — Analytic 0835**
- Platforms: Linux

Behavioral sequence of unauthorized privilege escalation via permission modification: (1) chmod/chown/setfacl process execution with suspicious parameters, (2) Targeting of critical system files or unusual permission values, (3) Correlation with non-privileged user context or unusual timing patterns, (4) Follow-on file access indicating successful permission bypass.

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
- AN0835: https://attack.mitre.org/detectionstrategies/DET0299#AN0835
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
