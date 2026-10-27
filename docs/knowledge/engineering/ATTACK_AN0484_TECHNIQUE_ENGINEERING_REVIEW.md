# Analytic 0484 Technique Engineering Review

## Reference

- Technique: **AN0484 — Analytic 0484**

Forged web cookies on Windows endpoints can be detected by monitoring unusual modifications of browser cookie stores (e.g., Chrome SQLite DB, Edge cache) by processes outside of browsers, followed by authentication events to SaaS or IaaS services. Defenders may observe processes writing directly to cookie storage paths or injecting tokens into browser sessions.

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
- AN0484: https://attack.mitre.org/detectionstrategies/DET0171#AN0484
- Reviewed: 2026-10-27
