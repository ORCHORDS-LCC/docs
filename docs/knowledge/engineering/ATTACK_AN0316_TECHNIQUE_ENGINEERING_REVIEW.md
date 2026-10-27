# Analytic 0316 Technique Engineering Review

## Reference

- Technique: **AN0316 — Analytic 0316**

Detects AS-REP roasting attempts by monitoring for Kerberos AS-REQ/AS-REP authentication patterns where preauthentication is disabled (Event ID 4768 with Pre-Auth Type 0). Correlates these requests with subsequent service ticket activity (Event ID 4769) and anomalies such as requests using weak RC4 encryption (etype 0x17). Excessive enumeration of accounts with 'Do not require Kerberos preauthentication' set in Active Directory is another key detection point.

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
- AN0316: https://attack.mitre.org/detectionstrategies/DET0113#AN0316
- Reviewed: 2026-10-27
