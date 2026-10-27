# Embargo Technique Platform Profile

## Reference

- Technique: **S1247 — Embargo**
- Platforms named in the source: ESXi, Linux, Windows

Embargo is a ransomware variant written in Rust that has been active since at least May 2024. Embargo ransomware operations are associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Embargo ransomware has been known to be delivered through a loader known as MDeployer which also leverages a malware component known as MS4Killer that facilitates termination of processes operating on the victim hosts. Embargo is also reportedly a Ransomware as a Service (RaaS).

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
- S1247: https://attack.mitre.org/software/S1247
- Reviewed: 2026-10-27
