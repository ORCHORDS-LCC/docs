# Analytic 1093 Technique Engineering Review

## Reference

- Technique: **AN1093 — Analytic 1093**

Detects anomalous ARP cache changes and unsolicited ARP broadcasts using unified logs and packet capture. Behavioral detection includes multiple IP addresses mapped to the same MAC address and repeated gratuitous ARP traffic.

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
- AN1093: https://attack.mitre.org/detectionstrategies/DET0387#AN1093
- Reviewed: 2026-10-27
