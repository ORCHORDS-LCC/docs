# AN0096 Analytic 0096 Outcome Lesson

## Authoritative description

- Technique: **AN0096 — Analytic 0096**
- Platforms: Linux

Detects execution of common process enumeration utilities (e.g., ps, top, htop) or access to /proc with suspicious ancestry. Correlates command usage with interactive shell context and user role.

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
- AN0096: https://attack.mitre.org/detectionstrategies/DET0034#AN0096
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
