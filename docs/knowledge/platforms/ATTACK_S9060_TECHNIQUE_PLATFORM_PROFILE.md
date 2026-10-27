# MiniBus Technique Platform Profile

## Reference

- Technique: **S9060 — MiniBus**
- Platforms named in the source: Windows

MiniBus is a custom backdoor used for command execution, data discovery, gathering, and exfiltration. MiniBus has utilized Azure Cloud Infrastructure and unique adversary-controlled domains for command and control. MiniBus is an updated platform to its predecessor MiniBike and was first observed in August 2023. MiniBus has been affiliated with the cyber espionage threat group NIMBUS MANTICORE.

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
- S9060: https://attack.mitre.org/software/S9060
- Reviewed: 2026-10-27
