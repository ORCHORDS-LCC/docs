# Analytic 0560 Technique Engineering Review

## Reference

- Technique: **AN0560 — Analytic 0560**

Execution of `ifconfig`, `ip a`, or access to `/proc/net/` indicating collection of local interface and route configuration.

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
- AN0560: https://attack.mitre.org/detectionstrategies/DET0195#AN0560
- Reviewed: 2026-10-27
