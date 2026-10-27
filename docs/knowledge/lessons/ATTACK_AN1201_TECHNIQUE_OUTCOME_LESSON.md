# AN1201 Analytic 1201 Outcome Lesson

## Authoritative description

- Technique: **AN1201 — Analytic 1201**
- Platforms: IaaS

Detects attempts to access or enumerate cloud password/secrets storage services such as AWS Secrets Manager, Azure Key Vault, or GCP Secret Manager. Monitors API calls for abnormal enumeration or bulk retrieval of secrets.

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
- AN1201: https://attack.mitre.org/detectionstrategies/DET0430#AN1201
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
