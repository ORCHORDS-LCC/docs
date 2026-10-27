# LLMNR/NBT-NS Poisoning Mitigation Technique Engineering Review

## Reference

- Technique: **T1171 — LLMNR/NBT-NS Poisoning Mitigation**

Disable LLMNR and NetBIOS in local computer security settings or by group policy if they are not needed within an environment. Use host-based security software to block LLMNR/NetBIOS traffic. Enabling SMB Signing can stop NTLMv2 relay attacks.

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
- T1171: https://attack.mitre.org/mitigations/T1171
- Reviewed: 2026-10-27
