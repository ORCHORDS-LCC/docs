# Analytic 0223 Technique Engineering Review

## Reference

- Technique: **AN0223 — Analytic 0223**

Adversary targets cloud-hosted public endpoints. Chain: (1) ALB/ELB/Cloud LB logs show exploit-like inputs or error spikes → (2) workload spawns shell or reaches metadata API → (3) egress to new external hosts.

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
- AN0223: https://attack.mitre.org/detectionstrategies/DET0080#AN0223
- Reviewed: 2026-10-27
