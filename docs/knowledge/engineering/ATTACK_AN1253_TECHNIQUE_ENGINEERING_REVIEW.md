# Analytic 1253 Technique Engineering Review

## Reference

- Technique: **AN1253 — Analytic 1253**

A process (often after stealing/creating a token) calls CreateProcessWithTokenW/CreateProcessAsUserW or uses runas to spawn a **new** process whose security context (SID/LogonId/IntegrityLevel) differs from its parent. Chain: (1) suspicious command/API → (2) privileged handle or token duplication/open → (3) new child process running as another user / higher integrity → (4) optional follow‑on privileged/lateral actions.

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
- AN1253: https://attack.mitre.org/detectionstrategies/DET0456#AN1253
- Reviewed: 2026-10-27
