# Analytic 0340 Technique Engineering Review

## Reference

- Technique: **AN0340 — Analytic 0340**

Creation or modification of Login Items using AppleScript or Service Management Framework. Detection focuses on file creation/modification of `backgrounditems.btm`, new executables in `Contents/Library/LoginItems/`, use of `SMLoginItemSetEnabled` API, or suspicious processes triggered post-login without user interaction. Behavioral pivot includes anomalous AppleEvents, suspicious parent-child process pairs, and login-triggered execution chains.

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
- AN0340: https://attack.mitre.org/detectionstrategies/DET0121#AN0340
- Reviewed: 2026-10-27
