# LockBit 2.0 Technique Engineering Review

## Reference

- Technique: **S1199 — LockBit 2.0**

LockBit 2.0 is an affiliate-based Ransomware-as-a-Service (RaaS) that has been in use since at least June 2021 as the successor to LockBit Ransomware. LockBit 2.0 has versions capable of infecting Windows and VMware ESXi virtual machines, and has been observed targeting multiple industry verticals globally.

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
- S1199: https://attack.mitre.org/software/S1199
- Reviewed: 2026-10-27
