# GoldFinder Technique Platform Profile

## Reference

- Technique: **S0597 — GoldFinder**
- Platforms named in the source: Windows

GoldFinder is a custom HTTP tracer tool written in Go that logs the route a packet takes between a compromised network and a C2 server. It can be used to inform threat actors of potential points of discovery or logging of their actions, including C2 related to other malware. GoldFinder was discovered in early 2021 during an investigation into the SolarWinds Compromise by APT29.

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
- S0597: https://attack.mitre.org/software/S0597
- Reviewed: 2026-10-27
