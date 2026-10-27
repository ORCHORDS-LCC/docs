# ZLib Technique Engineering Review

## Reference

- Technique: **S0086 — ZLib**

ZLib is a full-featured backdoor that was used as a second-stage implant during Operation Dust Storm since at least 2014. ZLib is malware and should not be confused with the legitimate compression library from which its name is derived.

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
- S0086: https://attack.mitre.org/software/S0086
- Reviewed: 2026-10-27
