# The Gentlemen Ransomware Technique Platform Profile

## Reference

- Technique: **S9051 — The Gentlemen Ransomware**
- Platforms named in the source: macOS, Linux, Windows, IaaS, ESXi, Network Devices

The Gentlemen Ransomware is a ransomware-as-a-service (RaaS). The Gentlemen Ransomware has been written in Go programming language and has utilized Garble to obfuscate its code to target Windows environments. The Gentlemen Ransomware is capable of executing its’ OS lockers in Windows, Linux, NAS, BSD and ESXi environments. The Gentlemen Ransomware was first observed in mid-2025 as a closed ransomware and shortly later emerged as a RaaS to affiliates in September 2025. The Gentlemen Ransomware has been affiliated with the threat group The Gentlemen.

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
- S9051: https://attack.mitre.org/software/S9051
- Reviewed: 2026-10-27
