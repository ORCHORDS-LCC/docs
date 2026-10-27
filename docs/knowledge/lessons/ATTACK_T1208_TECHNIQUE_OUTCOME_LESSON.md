# T1208 Kerberoasting Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1208 — Kerberoasting Mitigation**

Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire. Also consider using Group Managed Service Accounts or another third party product such as password vaulting. Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators. Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.

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
- T1208: https://attack.mitre.org/mitigations/T1208
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
