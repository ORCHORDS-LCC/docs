# Clipboard Data Technique Engineering Review

## Reference

- Technique: **T1115 — Clipboard Data**

Adversaries may collect data stored in the clipboard from users copying information within or between applications. For example, on Windows adversaries can access clipboard data by using clip.exe or Get-Clipboard. Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., Transmitted Data Manipulation). macOS and Linux also have commands, such as pbpaste, to grab clipboard contents.

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
- T1115: https://attack.mitre.org/techniques/T1115
- Reviewed: 2026-10-27
