# Analytic 0015 Technique Platform Profile

## Reference

- Technique: **AN0015 — Analytic 0015**
- Platforms named in the source: Network Devices

From a defender’s perspective, suspicious bridging is observed when network devices begin allowing traffic that contradicts existing segmentation or access policies. Observable behaviors include sudden modifications to ACLs or firewall rules, unusual cross-boundary traffic flows (e.g., east-west communications across separated VLANs), or simultaneous ingress/egress anomalies. Multi-event correlation is key: configuration changes on a router/firewall followed by unexpected traffic patterns, especially from unusual sources, is a strong indicator of compromise.

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
- AN0015: https://attack.mitre.org/detectionstrategies/DET0006#AN0015
- Reviewed: 2026-10-27
