# BOLDMOVE Technique Engineering Review

## Reference

- Technique: **S1184 — BOLDMOVE**

BOLDMOVE is a type of backdoor malware written in C linked to People’s Republic of China operations from 2022 through 2023. BOLDMOVE includes both Windows and Linux variants, with some Linux variants specifically designed for FortiGate Firewall devices. BOLDMOVE is linked to zero-day exploitation of CVE-2022-42475 in FortiOSS SSL-VPNs. The record for BOLDMOVE only covers known Linux variants.

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
- S1184: https://attack.mitre.org/software/S1184
- Reviewed: 2026-10-27
