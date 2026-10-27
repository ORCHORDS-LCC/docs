# SLOTHFULMEDIA Technique Engineering Review

## Reference

- Technique: **S0533 — SLOTHFULMEDIA**

SLOTHFULMEDIA is a remote access Trojan written in C++ that has been used by an unidentified "sophisticated cyber actor" since at least January 2017. It has been used to target government organizations, defense contractors, universities, and energy companies in Russia, India, Kazakhstan, Kyrgyzstan, Malaysia, Ukraine, and Eastern Europe. In October 2020, Kaspersky Labs assessed SLOTHFULMEDIA is part of an activity cluster it refers to as "IAmTheKing". ESET also noted code similarity between SLOTHFULMEDIA and droppers used by a group it refers to as "PowerPool".

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
- S0533: https://attack.mitre.org/software/S0533
- Reviewed: 2026-10-27
