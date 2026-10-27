# Analytic 1098 Technique Engineering Review

## Reference

- Technique: **AN1098 — Analytic 1098**

Detect runtime manipulation by monitoring system calls for modifications to shared libraries, ELF binaries, or environment variables that affect how data is displayed. Look for suspicious writes to application directories and mismatch in binary integrity baselines.

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
- AN1098: https://attack.mitre.org/detectionstrategies/DET0391#AN1098
- Reviewed: 2026-10-27
