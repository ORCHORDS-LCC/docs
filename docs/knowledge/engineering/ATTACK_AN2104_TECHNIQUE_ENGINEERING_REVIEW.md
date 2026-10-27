# Analytic 2104 Technique Engineering Review

## Reference

- Technique: **AN2104 — Analytic 2104**

Successful CAPTCHA completion does not expose whether the challenge was solved manually, through automated tooling, through an AI-enabled solver, or through a third-party human-solving service. Providers may independently classify associated sessions as automated or bot-like, but this identifies suspicious automation rather than the method used to complete the CAPTCHA.

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
- AN2104: https://attack.mitre.org/detectionstrategies/DET0937#AN2104
- Reviewed: 2026-10-27
