# AN1473 Analytic 1473 Outcome Lesson

## Authoritative description

- Technique: **AN1473 — Analytic 1473**
- Platforms: SaaS

Detects anomalous CI/CD workflow execution originating from forked repositories, with pull request (PR) metadata or commit messages containing suspicious patterns (e.g., encoded payloads), coupled with the use of insecure pipeline triggers like `pull_request_target` or excessive API usage of CI/CD secrets. Correlation with unusual artifact generation or secret exfiltration via encoded or external network destination URLs confirms suspicious behavior.

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
- AN1473: https://attack.mitre.org/detectionstrategies/DET0533#AN1473
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
