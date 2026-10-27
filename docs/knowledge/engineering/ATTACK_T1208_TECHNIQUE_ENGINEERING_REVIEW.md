# Kerberoasting Mitigation Technique Engineering Review

## Reference

- Technique: **T1208 — Kerberoasting Mitigation**

Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire. Also consider using Group Managed Service Accounts or another third party product such as password vaulting. Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators. Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1208: https://attack.mitre.org/mitigations/T1208
- Reviewed: 2026-10-27
