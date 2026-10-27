# Qilin Technique Platform Profile

## Reference

- Technique: **S1242 — Qilin**
- Platforms named in the source: ESXi, Windows, Linux

Qilin is a ransomware family operated as a ransomware-as-a-service (RaaS) that has been active since at least 2022. It includes variants written in Go and Rust capable of targeting Windows, Linux, and VMware ESXi environments. Qilin shares functionality overlaps with Black Basta, REvil, and BlackCat ransomware. Qilin affiliates have targeted multiple entities worldwide with the majority of victims in the US, France, Canada, and the UK, primarily in the manufacturing, technology, financial services, and healthcare sectors.

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
- S1242: https://attack.mitre.org/software/S1242
- Reviewed: 2026-10-27
