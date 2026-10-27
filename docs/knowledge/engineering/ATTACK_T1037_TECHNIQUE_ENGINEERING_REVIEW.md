# Logon Scripts Mitigation Technique Engineering Review

## Reference

- Technique: **T1037 — Logon Scripts Mitigation**

Restrict write access to logon scripts to specific administrators. Prevent access to administrator accounts by mitigating Credential Access techniques and limiting account access and permissions of Valid Accounts. Identify and block potentially malicious software that may be executed through logon script modification by using whitelisting tools like AppLocker that are capable of auditing and/or blocking unknown programs.

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
- T1037: https://attack.mitre.org/mitigations/T1037
- Reviewed: 2026-10-27
