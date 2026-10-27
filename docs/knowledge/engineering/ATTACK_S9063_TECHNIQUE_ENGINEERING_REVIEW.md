# DEEPROOT Technique Engineering Review

## Reference

- Technique: **S9063 — DEEPROOT**

DEEPROOT is a Linux backdoor written in Golang. DEEPROOT is able to execute commands via a shell, enumerate systems, delete or download files, and exfiltrate data. DEEPROOT was first observed in 2025. DEEPROOT has been affiliated with the cyber espionage threat group NIMBUS MANTICORE.

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
- S9063: https://attack.mitre.org/software/S9063
- Reviewed: 2026-10-27
