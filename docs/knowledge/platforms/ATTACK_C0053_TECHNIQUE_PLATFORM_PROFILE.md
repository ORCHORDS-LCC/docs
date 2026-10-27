# FLORAHOX Activity Technique Platform Profile

## Reference

- Technique: **C0053 — FLORAHOX Activity**
- Platforms named in the source: not stated

FLORAHOX Activity is conducted using a hybrid operational relay box (ORB) network, which combines two types of infrastructure: compromised devices and leased Virtual Private Servers (VPS). The compromised devices include end-of-life routers and IoT devices, while VPS space is commercially leased and managed by ORB network administrators. This hybrid ORB network allows adversaries to proxy and obscure malicious traffic, making the source of the traffic more difficult to trace. The FLORAHOX ORB network has been leveraged by multiple cyber threat actors, including China-nexus actors like ZIRCONIUM. These adversaries conduct espionage campaigns through FLORAHOX Activity, relying on the ORB network's ability to funnel traffic through Tor nodes, provisioned VPS servers, and compromised routers to obfuscate malicious traffic.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0053: https://attack.mitre.org/campaigns/C0053
- Reviewed: 2026-10-27
