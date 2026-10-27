# Windows Registry Key Modification Technique Platform Profile

## Reference

- Technique: **DC0063 — Windows Registry Key Modification**
- Platforms named in the source: not stated

Changes made to an existing registry key or its values. These modifications can include altering permissions, modifying stored data, or updating configuration settings. *Data Collection Measures:* - Windows Event Logs - Event ID 4657 - Registry Value Modified: Logs changes to registry values, including modifications to startup entries, security settings, or system configurations. - Sysmon (System Monitor) for Windows - Sysmon Event ID 13 - Registry Value Set: Captures changes to specific registry values. - Sysmon Event ID 14 - Registry Key & Value Renamed: Logs renaming of registry keys, which may indicate evasion attempts. - Endpoint Detection and Response (EDR) Solutions - Monitor registry modifications for suspicious behavior.

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
- DC0063: https://attack.mitre.org/datacomponents/DC0063
- Reviewed: 2026-10-27
