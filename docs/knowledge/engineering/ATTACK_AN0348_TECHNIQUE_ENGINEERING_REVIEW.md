# Analytic 0348 Technique Engineering Review

## Reference

- Technique: **AN0348 — Analytic 0348**

ESXi shell (BusyBox) or VMware utilities (openssl, python if present) used to Base64/hex encode data from datastore or config files → followed by abnormal egress from the host (NSX/flow logs) with asymmetric bytes_out or HTTPS posts to non-management endpoints.

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
- AN0348: https://attack.mitre.org/detectionstrategies/DET0124#AN0348
- Reviewed: 2026-10-27
