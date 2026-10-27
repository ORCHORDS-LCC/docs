# Lateral Tool Transfer Technique Platform Profile

## Reference

- Technique: **T1570 — Lateral Tool Transfer**
- Platforms named in the source: ESXi, Linux, macOS, Windows

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., Ingress Tool Transfer) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation. Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over SMB/Windows Admin Shares to connected network shares or with authenticated connections via Remote Desktop Protocol. Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and ftp. In some cases, adversaries may be able to leverage Web Services such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.

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
- T1570: https://attack.mitre.org/techniques/T1570
- Reviewed: 2026-10-27
