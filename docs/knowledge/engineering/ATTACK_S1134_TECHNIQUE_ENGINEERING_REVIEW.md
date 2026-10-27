# DEADWOOD Technique Engineering Review

## Reference

- Technique: **S1134 — DEADWOOD**

DEADWOOD is wiper malware written in C++ using Boost libraries. DEADWOOD was first observed in an unattributed wiping event in Saudi Arabia in 2019, and has since been incorporated into Agrius operations.

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
- S1134: https://attack.mitre.org/software/S1134
- Reviewed: 2026-10-27
