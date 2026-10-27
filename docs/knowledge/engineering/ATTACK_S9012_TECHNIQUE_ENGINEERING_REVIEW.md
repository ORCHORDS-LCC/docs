# TRAILBLAZE Technique Engineering Review

## Reference

- Technique: **S9012 — TRAILBLAZE**

TRAILBLAZE is an in-memory dropper used to deploy the passive backdoor BRUSHFIRE. First reported in March 2025, TRAILBLAZE has been observed in operations attributed to People's Republic of China (PRC) state-sponsored affiliated actors, including UNC5221 and SYLVANITE.

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
- S9012: https://attack.mitre.org/software/S9012
- Reviewed: 2026-10-27
