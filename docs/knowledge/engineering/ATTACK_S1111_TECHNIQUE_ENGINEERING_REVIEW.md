# DarkGate Technique Engineering Review

## Reference

- Technique: **S1111 — DarkGate**

DarkGate first emerged in 2018 and has evolved into an initial access and data gathering tool associated with various criminal cyber operations. Written in Delphi and named "DarkGate" by its author, DarkGate is associated with credential theft, cryptomining, cryptotheft, and pre-ransomware actions. DarkGate use increased significantly starting in 2022 and is under active development by its author, who provides it as a Malware-as-a-Service offering.

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
- S1111: https://attack.mitre.org/software/S1111
- Reviewed: 2026-10-27
