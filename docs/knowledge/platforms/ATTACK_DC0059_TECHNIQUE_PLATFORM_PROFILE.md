# File Metadata Technique Platform Profile

## Reference

- Technique: **DC0059 — File Metadata**
- Platforms named in the source: not stated

Contextual information about a file, including attributes such as the file's name, size, type, content (e.g., signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other anomalies. Examples: - File Ownership and Permissions: Checking the owner and permissions of a critical configuration file like /etc/passwd on Linux or C:\Windows\System32\config\SAM on Windows. - Timestamps: Analyzing the creation, modification, and access timestamps of a file. - File Content and Signatures: Extracting the headers of an executable file to verify its signature or detect packing/obfuscation. - File Attributes: Analyzing attributes like hidden, system, or read-only flags in Windows. - File Hashes: Generating MD5, SHA-1, or SHA-256 hashes of files to compare against threat intelligence feeds. - File Location: Monitoring files located in unusual directories or paths, such as temporary or user folders.

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
- DC0059: https://attack.mitre.org/datacomponents/DC0059
- Reviewed: 2026-10-27
