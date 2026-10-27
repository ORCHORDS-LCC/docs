# AN0420 Analytic 0420 Outcome Lesson

## Authoritative description

- Technique: **AN0420 — Analytic 0420**
- Platforms: Windows

Forged SAML tokens may be used on Windows systems to authenticate to federated apps without normal Kerberos activity. Defenders may detect anomalous event correlation, where access to SaaS/O365 via SAML occurs without prior TGT requests or user logons.

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
- AN0420: https://attack.mitre.org/detectionstrategies/DET0148#AN0420
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
