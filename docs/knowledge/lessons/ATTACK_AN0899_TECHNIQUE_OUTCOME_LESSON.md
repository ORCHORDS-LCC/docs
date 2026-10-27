# AN0899 Analytic 0899 Outcome Lesson

## Authoritative description

- Technique: **AN0899 — Analytic 0899**
- Platforms: Identity Provider

Adversaries create user accounts via identity provider APIs or admin portals (e.g., Azure AD, Okta). These accounts may be assigned elevated privileges or used in chained authentication. Detection monitors Add User activity from suspicious IPs or automation sources, followed by role/permission escalation.

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
- AN0899: https://attack.mitre.org/detectionstrategies/DET0319#AN0899
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
