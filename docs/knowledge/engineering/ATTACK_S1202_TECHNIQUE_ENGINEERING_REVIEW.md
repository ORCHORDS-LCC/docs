# LockBit 3.0 Technique Engineering Review

## Reference

- Technique: **S1202 — LockBit 3.0**

LockBit 3.0 is an evolution of the LockBit Ransomware-as-a-Service (RaaS) offering with similarities to BlackMatter and BlackCat ransomware. LockBit 3.0 has been in use since at least June 2022 and features enhanced defense evasion and exfiltration tactics, robust encryption methods for Windows and VMware ESXi systems, and a more refined RaaS structure over its predecessors such as LockBit 2.0.

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
- S1202: https://attack.mitre.org/software/S1202
- Reviewed: 2026-10-27
