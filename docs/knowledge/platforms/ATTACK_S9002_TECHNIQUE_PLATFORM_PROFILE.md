# Diskpart Technique Platform Profile

## Reference

- Technique: **S9002 — Diskpart**
- Platforms named in the source: Windows

Diskpart is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks. Adversaries may abuse Diskpart to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using Diskpart to conduct Discovery techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.

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
- S9002: https://attack.mitre.org/software/S9002
- Reviewed: 2026-10-27
