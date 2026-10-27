# MiniBike Technique Platform Profile

## Reference

- Technique: **S9059 — MiniBike**
- Platforms named in the source: Windows

MiniBike is a custom backdoor written in C++ designed for command execution, data discovery, gathering, and exfiltration. MiniBike has been known to communicate with the C2 using Azure Cloud Infrastructure. MiniBike was first observed in 2022. MiniBike has been affiliated with the cyber espionage threat group NIMBUS MANTICORE.

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
- S9059: https://attack.mitre.org/software/S9059
- Reviewed: 2026-10-27
