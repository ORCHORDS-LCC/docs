# Steal Application Specific Passwords Technique Engineering Review

## Reference

- Technique: **T1697 — Steal Application Specific Passwords**

Adversaries may steal Application Specific Passwords (ASPs) to gain access to Valid Accounts, bypassing multifactor authentication (MFA) methods. ASPs are passwords typically used to give third-party applications or legacy devices (which do not support MFA methods) account access. An adversary may socially engineer a user into providing an ASP (using methods like Phishing for Information), generate an ASP for an already compromised account, or obtain an ASP stored on a system. Afterward, adversaries may use the ASP to access Valid Accounts and, in some cases, maintain Persistence, bypassing any form of MFA set on the account.

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
- T1697: https://attack.mitre.org/techniques/T1697
- Reviewed: 2026-10-27
