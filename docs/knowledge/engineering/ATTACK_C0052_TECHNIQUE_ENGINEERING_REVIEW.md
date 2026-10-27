# SPACEHOP Activity Technique Engineering Review

## Reference

- Technique: **C0052 — SPACEHOP Activity**

SPACEHOP Activity is conducted through commercially leased Virtual Private Servers (VPS), otherwise known as provisioned Operational Relay Box (ORB) networks. The network leveraged for SPACEHOP Activity enabled China-nexus cyber threat actors – such as APT5 and Ke3chang – to perform network reconnaissance scanning and vulnerability exploitation. SPACEHOP Activity has historically targeted entities in North America, Europe, and the Middle East.

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
- C0052: https://attack.mitre.org/campaigns/C0052
- Reviewed: 2026-10-27
