# Analytic 0390 Technique Engineering Review

## Reference

- Technique: **AN0390 — Analytic 0390**

Detects credential interception via malicious LD_PRELOAD-based shared libraries loaded into ssh, sudo, or scp processes. Correlates environment variable injection, unexpected library loads, and memory patching behavior.

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
- AN0390: https://attack.mitre.org/detectionstrategies/DET0139#AN0390
- Reviewed: 2026-10-27
