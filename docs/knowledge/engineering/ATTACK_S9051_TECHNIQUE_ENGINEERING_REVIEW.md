# The Gentlemen Ransomware Technique Engineering Review

## Reference

- Technique: **S9051 — The Gentlemen Ransomware**

The Gentlemen Ransomware is a ransomware-as-a-service (RaaS). The Gentlemen Ransomware has been written in Go programming language and has utilized Garble to obfuscate its code to target Windows environments. The Gentlemen Ransomware is capable of executing its’ OS lockers in Windows, Linux, NAS, BSD and ESXi environments. The Gentlemen Ransomware was first observed in mid-2025 as a closed ransomware and shortly later emerged as a RaaS to affiliates in September 2025. The Gentlemen Ransomware has been affiliated with the threat group The Gentlemen.

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
- S9051: https://attack.mitre.org/software/S9051
- Reviewed: 2026-10-27
