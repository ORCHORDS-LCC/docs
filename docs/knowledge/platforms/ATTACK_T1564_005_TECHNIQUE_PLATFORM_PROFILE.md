# Hidden File System Technique Platform Profile

## Reference

- Technique: **T1564.005 — Hidden File System**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may use a hidden file system to conceal malicious activity from users and security tools. File systems provide a structure to store and access data from physical storage. Typically, a user engages with a file system through applications that allow them to access files and directories, which are an abstraction from their physical location (ex: disk sector). Standard file systems include FAT, NTFS, ext4, and APFS. File systems can also contain other structures, such as the Volume Boot Record (VBR) and Master File Table (MFT) in NTFS. Adversaries may use their own abstracted file system, separate from the standard file system present on the infected system. In doing so, adversaries can hide the presence of malicious components and file input/output from security tools. Hidden file systems, sometimes referred to as virtual file systems, can be implemented in numerous ways. One implementation would be to store a file system in reserved disk space unused by disk structures or standard file system partitions. Another implementation could be for an adversary to drop their own portable partition image as a file on top of the standard file system. Adversaries may also fragment files across the existing file system structure in non-standard ways.

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
- T1564.005: https://attack.mitre.org/techniques/T1564/005
- Reviewed: 2026-10-27
