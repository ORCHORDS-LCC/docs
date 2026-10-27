# AN0366 Analytic 0366 Outcome Lesson

## Authoritative description

- Technique: **AN0366 — Analytic 0366**
- Platforms: IaaS

Detection of suspicious access to cloud-native secret management systems (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, HashiCorp Vault). Focuses on abnormal secret retrieval activity, such as secrets being accessed by unusual identities, from unexpected regions, outside business hours, or at high volume. Correlates API calls to secret retrieval with surrounding authentication events, role assumptions, and anomalous execution patterns.

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
- AN0366: https://attack.mitre.org/detectionstrategies/DET0130#AN0366
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
