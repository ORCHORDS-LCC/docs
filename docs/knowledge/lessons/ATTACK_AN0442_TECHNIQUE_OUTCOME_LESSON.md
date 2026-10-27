# AN0442 Analytic 0442 Outcome Lesson

## Authoritative description

- Technique: **AN0442 — Analytic 0442**
- Platforms: IaaS

Monitor for unauthorized or unusual modifications to cloud resource hierarchies such as AWS Organizations or Azure Management Groups. Defenders may observe anomalous calls to APIs like `LeaveOrganization`, `CreateAccount`, `MoveAccount`, or Azure subscription transfers. Correlate account activity with administrative role assignments, tenant transfers, or new subscription creation that deviates from organizational baselines. Multi-event correlation should track role elevation followed by hierarchy modifications within a short time window.

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
- AN0442: https://attack.mitre.org/detectionstrategies/DET0155#AN0442
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
