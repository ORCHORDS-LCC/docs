# File Access Technique Platform Profile

## Reference

- Technique: **DC0055 — File Access**
- Platforms named in the source: not stated

To events where a file is opened or accessed, making its contents available to the requester. This includes reading, executing, or interacting with files by authorized or unauthorized entities. Examples include logging file access events (e.g., Windows Event ID 4663), monitoring file reads, and detecting unusual file access patterns. Examples: - File Read Operations: A user opens a sensitive document (e.g., financial_report.xlsx) on a shared drive. - File Execution: A script or executable file is accessed and executed (e.g., malware.exe is run from a temporary directory). - Unauthorized File Access: An unauthorized user attempts to access a protected configuration file (e.g., `/etc/passwd` on Linux or `System32` files on Windows). - File Access Patterns: Bulk access to multiple files in a short time (e.g., mass access to documents on a file server). - File Access via Network: Files on a network share are accessed remotely (e.g., logs of SMB file access).

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
- DC0055: https://attack.mitre.org/datacomponents/DC0055
- Reviewed: 2026-10-27
