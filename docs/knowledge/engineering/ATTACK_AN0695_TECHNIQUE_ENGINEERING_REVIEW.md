# Analytic 0695 Technique Engineering Review

## Reference

- Technique: **AN0695 — Analytic 0695**

Detects adversarial use of cloud-native APIs (e.g., AWS IAM, Azure RBAC, GCP Identity) to enumerate cloud group memberships or policy mappings via unauthorized sessions or scripts.

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
- AN0695: https://attack.mitre.org/detectionstrategies/DET0251#AN0695
- Reviewed: 2026-10-27
