# Direct Volume Access Technique Platform Profile

## Reference

- Technique: **T1006 — Direct Volume Access**
- Platforms named in the source: Network Devices, Windows

Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell. Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and esentutl) to create shadow copies or backups of data from system volumes.

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
- T1006: https://attack.mitre.org/techniques/T1006
- Reviewed: 2026-10-27
