# Drive Access Technique Platform Profile

## Reference

- Technique: **DC0054 — Drive Access**
- Platforms named in the source: not stated

Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive. This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing files within an assigned drive letter (e.g., `C:\`, `/mnt/drive`) or mount point. Examples: - Removable Drive Insertion: A USB drive is inserted, assigned the letter `F:\`, and files are accessed. - Network Drive Mounting: A network share `\\server\share` is mapped to the drive `Z:\`. - External Hard Drive Access: An external drive is connected, mounted at `/mnt/backup`, and accessed for copying files. - System Volume Access: The system volume `C:\` is accessed for modifications to critical files. - Cloud-Synced Drives: Cloud storage drives like OneDrive or Google Drive are accessed via local mounts.

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
- DC0054: https://attack.mitre.org/datacomponents/DC0054
- Reviewed: 2026-10-27
