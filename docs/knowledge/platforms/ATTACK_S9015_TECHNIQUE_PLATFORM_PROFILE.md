# BRICKSTORM Technique Platform Profile

## Reference

- Technique: **S9015 — BRICKSTORM**
- Platforms named in the source: ESXi, Linux, Network Devices, Windows

BRICKSTORM is a cross-platform backdoor with variants written in Go and Rust that facilitates command and control, the ingress transfer of other malware, and the exfiltration of data. BRICKSTORM has also been created from a .NET application using ahead-of-time (AOT) compilation to blend in within victim environments. BRICKSTORM was first observed in April 2024. BRICKSTORM has previously been leveraged by People's Republic of China (PRC) state-nexus actors identified as UNC6201, UNC5221, WARP PANDA, PunyToad, and SYLVANITE.

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
- S9015: https://attack.mitre.org/software/S9015
- Reviewed: 2026-10-27
