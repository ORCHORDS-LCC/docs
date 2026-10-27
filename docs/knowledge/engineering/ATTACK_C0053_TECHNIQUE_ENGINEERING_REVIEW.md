# FLORAHOX Activity Technique Engineering Review

## Reference

- Technique: **C0053 — FLORAHOX Activity**

FLORAHOX Activity is conducted using a hybrid operational relay box (ORB) network, which combines two types of infrastructure: compromised devices and leased Virtual Private Servers (VPS). The compromised devices include end-of-life routers and IoT devices, while VPS space is commercially leased and managed by ORB network administrators. This hybrid ORB network allows adversaries to proxy and obscure malicious traffic, making the source of the traffic more difficult to trace. The FLORAHOX ORB network has been leveraged by multiple cyber threat actors, including China-nexus actors like ZIRCONIUM. These adversaries conduct espionage campaigns through FLORAHOX Activity, relying on the ORB network's ability to funnel traffic through Tor nodes, provisioned VPS servers, and compromised routers to obfuscate malicious traffic.

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
- C0053: https://attack.mitre.org/campaigns/C0053
- Reviewed: 2026-10-27
