# Drive Creation Technique Platform Profile

## Reference

- Technique: **DC0042 — Drive Creation**
- Platforms named in the source: not stated

The activity of assigning a new drive letter or creating a mount point for a data storage device, such as a USB, network share, or external hard drive, enabling access to its content on a host system. Examples: - USB Drive Insertion: A USB drive is plugged in and automatically assigned the letter `E:\` on a Windows machine. - Network Drive Mapping: A network share `\\server\share` is mapped to the drive `Z:\`. - Virtual Drive Creation: A virtual disk is mounted on `/mnt/virtualdrive` using an ISO image or a virtual hard disk (VHD). - Cloud Storage Mounting: Google Drive is mounted as `G:\` on a Windows machine using a cloud sync tool. - External Storage Integration: An external HDD or SSD is connected and assigned `/mnt/external` on a Linux system..

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
- DC0042: https://attack.mitre.org/datacomponents/DC0042
- Reviewed: 2026-10-27
