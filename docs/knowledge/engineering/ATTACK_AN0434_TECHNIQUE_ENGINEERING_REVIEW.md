# Analytic 0434 Technique Engineering Review

## Reference

- Technique: **AN0434 — Analytic 0434**

Non-standard or rare users/locations issue CLI commands like "show clock detail" or "show timezone"; optionally followed by configuration of time/timezone or NTP sources. AAA/TACACS+ accounting and syslog correlate execution to identity, source IP, and privilege level.

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
- AN0434: https://attack.mitre.org/detectionstrategies/DET0151#AN0434
- Reviewed: 2026-10-27
