# Raspberry Robin Technique Engineering Review

## Reference

- Technique: **S1130 — Raspberry Robin**

Raspberry Robin is initial access malware first identified in September 2021, and active through early 2024. The malware is notable for spreading via infected USB devices containing a malicious LNK object that, on execution, retrieves remote hosted payloads for installation. Raspberry Robin has been widely used against various industries and geographies, and as a precursor to information stealer, ransomware, and other payloads such as SocGholish, Cobalt Strike, IcedID, and Bumblebee. The DLL componenet in the Raspberry Robin infection chain is also referred to as "Roshtyak." The name "Raspberry Robin" is used to refer to both the malware as well as the threat actor associated with its use, although the Raspberry Robin operators are also tracked as Storm-0856 by some vendors.

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
- S1130: https://attack.mitre.org/software/S1130
- Reviewed: 2026-10-27
