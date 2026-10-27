# Analytic 1197 Technique Engineering Review

## Reference

- Technique: **AN1197 — Analytic 1197**

Detects the modification or addition of Launch Agents or Startup Items to establish persistence. Adversaries may write plist or executable files to ~/Library/LaunchAgents/, /Library/StartupItems/, or similar directories and configure them to run at user or system boot. Detection requires correlating file creation or modification events with subsequent user logon or boot-time process execution.

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
- AN1197: https://attack.mitre.org/detectionstrategies/DET0429#AN1197
- Reviewed: 2026-10-27
