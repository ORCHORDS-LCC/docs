# J-magic Campaign Technique Engineering Review

## Reference

- Technique: **C0050 — J-magic Campaign**

The J-magic Campaign was active from mid-2023 to at least mid-2024 and featured the use of the J-magic backdoor, a custom cd00r variant tailored for use against Juniper routers. The J-magic Campaign targeted Junos OS routers serving as VPN gateways primarily in the semiconductor, energy, manufacturing, and IT sectors.

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
- C0050: https://attack.mitre.org/campaigns/C0050
- Reviewed: 2026-10-27
