# Analytic 0184 Technique Engineering Review

## Reference

- Technique: **AN0184 — Analytic 0184**

Adversary installs or modifies IIS components (ISAPI filters, extensions, or modules) using DLL files registered via configuration changes or administrative tools like AppCmd.exe. These components intercept or manipulate HTTP requests/responses for persistence or C2.

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
- AN0184: https://attack.mitre.org/detectionstrategies/DET0068#AN0184
- Reviewed: 2026-10-27
