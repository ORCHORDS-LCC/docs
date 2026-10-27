# Analytic 1534 Technique Engineering Review

## Reference

- Technique: **AN1534 — Analytic 1534**

Detection focuses on identifying unauthorized file creation or modification within `/etc/emond.d/rules/` or `/private/var/db/emondClients`, which indicate attempts to register a malicious emond rule. Correlate with process execution of `/sbin/emond` and any launched commands it invokes, especially during boot or login events. Anomalies may include rules created by non-root users or unexpected shell commands executed by emond.

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
- AN1534: https://attack.mitre.org/detectionstrategies/DET0555#AN1534
- Reviewed: 2026-10-27
