# Analytic 0791 Technique Engineering Review

## Reference

- Technique: **AN0791 — Analytic 0791**

A remote DCOM invocation by a privileged account using RPC (port 135), followed by abnormal process instantiation or module loading on the remote system indicative of code execution.

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
- AN0791: https://attack.mitre.org/detectionstrategies/DET0285#AN0791
- Reviewed: 2026-10-27
