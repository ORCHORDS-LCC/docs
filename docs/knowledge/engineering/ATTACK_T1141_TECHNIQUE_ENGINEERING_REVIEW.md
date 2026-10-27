# Input Prompt Mitigation Technique Engineering Review

## Reference

- Technique: **T1141 — Input Prompt Mitigation**

This technique exploits users' tendencies to always supply credentials when prompted, which makes it very difficult to mitigate. Use user training as a way to bring awareness and raise suspicion for potentially malicious events (ex: Office documents prompting for credentials).

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
- T1141: https://attack.mitre.org/mitigations/T1141
- Reviewed: 2026-10-27
