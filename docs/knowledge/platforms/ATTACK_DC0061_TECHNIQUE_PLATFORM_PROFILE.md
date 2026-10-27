# File Modification Technique Platform Profile

## Reference

- Technique: **DC0061 — File Modification**
- Platforms named in the source: not stated

Changes made to a file, including updates to its contents, metadata, access permissions, or attributes. These modifications may indicate legitimate activity (e.g., software updates) or unauthorized changes (e.g., tampering, ransomware, or adversarial modifications). Examples: - Content Modifications: Changes to the content of a configuration file, such as modifying `/etc/ssh/sshd_config` on Linux or `C:\Windows\System32\drivers\etc\hosts` on Windows. - Permission Changes: Altering file permissions to allow broader access, such as changing a file from `644` to `777` on Linux or modifying NTFS permissions on Windows. - Attribute Modifications: Changing a file's attributes to hidden, read-only, or system on Windows. - Timestamp Manipulation: Adjusting a file's creation or modification timestamp using tools like `touch` in Linux or timestomping tools on Windows. - Software or System File Changes: Modifying system files such as `boot.ini`, kernel modules, or application binaries.

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
- DC0061: https://attack.mitre.org/datacomponents/DC0061
- Reviewed: 2026-10-27
