# Stuxnet Technique Engineering Review

## Reference

- Technique: **S0603 — Stuxnet**

Stuxnet was the first publicly reported malware to specifically target industrial control systems devices. Stuxnet is a large and complex malware that utilized multiple behaviors, including numerous zero-day vulnerabilities, a sophisticated Windows rootkit, and network infection routines. Stuxnet was discovered in 2010, with some components being used as early as November 2008.

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
- S0603: https://attack.mitre.org/software/S0603
- Reviewed: 2026-10-27
