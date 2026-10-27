# Analytic 1356 Technique Engineering Review

## Reference

- Technique: **AN1356 — Analytic 1356**

Defenders should monitor for anomalous or unauthorized changes to cloud compute configurations that alter quotas, tenant-wide policies, subscription associations, or allowed deployment regions. From a defender’s perspective, suspicious behavior chains include a sudden increase in compute quota requests followed by new instance or resource creation, policy modifications that weaken security restrictions, or enabling previously unused/unsupported cloud regions. Correlation across identity, configuration, and subsequent provisioning logs is critical to distinguish legitimate administrative activity from adversarial abuse.

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
- AN1356: https://attack.mitre.org/detectionstrategies/DET0492#AN1356
- Reviewed: 2026-10-27
