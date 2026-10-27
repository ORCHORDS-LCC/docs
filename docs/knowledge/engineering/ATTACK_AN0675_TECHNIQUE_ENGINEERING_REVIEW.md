# Analytic 0675 Technique Engineering Review

## Reference

- Technique: **AN0675 — Analytic 0675**

Detects forged Kerberos Silver Tickets by identifying anomalous Kerberos service ticket activity such as malformed fields in logon events, TGS requests without interaction with the KDC, and access attempts using service accounts outside expected hosts/resources. Also monitors suspicious processes accessing LSASS memory for credential dumping.

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
- AN0675: https://attack.mitre.org/detectionstrategies/DET0241#AN0675
- Reviewed: 2026-10-27
