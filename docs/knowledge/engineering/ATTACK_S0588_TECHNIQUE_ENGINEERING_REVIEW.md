# GoldMax Technique Engineering Review

## Reference

- Technique: **S0588 — GoldMax**

GoldMax is a second-stage C2 backdoor written in Go with Windows and Linux variants that are nearly identical in functionality. GoldMax was discovered in early 2021 during the investigation into the SolarWinds Compromise, and has likely been used by APT29 since at least mid-2019. GoldMax uses multiple defense evasion techniques, including avoiding virtualization execution and masking malicious traffic.

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
- S0588: https://attack.mitre.org/software/S0588
- Reviewed: 2026-10-27
