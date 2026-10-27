# Analytic 0328 Technique Engineering Review

## Reference

- Technique: **AN0328 — Analytic 0328**

Links inbound network access to SSHD/SMB/NFS/Databases or custom daemons with subsequent daemon crash/restart, core dump, or spawning of shells/reverse shells from the service context, indicating remote exploitation.

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
- AN0328: https://attack.mitre.org/detectionstrategies/DET0118#AN0328
- Reviewed: 2026-10-27
