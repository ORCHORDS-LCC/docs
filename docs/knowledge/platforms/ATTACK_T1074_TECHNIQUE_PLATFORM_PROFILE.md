# Data Staged Mitigation Technique Platform Profile

## Reference

- Technique: **T1074 — Data Staged Mitigation**
- Platforms named in the source: not stated

Identify system utilities, remote access or third-party tools, users or potentially malicious software that may be used to store compressed or encrypted data in a publicly writeable directory, central location, or commonly used staging directories (e.g. recycle bin) that is indicative of non-standard behavior, and audit and/or block them by using file integrity monitoring tools where appropriate. Consider applying data size limits or blocking file writes of common compression and encryption utilities such as 7zip, RAR, ZIP, or zlib on frequently used staging directories or central locations and monitor attempted violations of those restrictions.

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
- T1074: https://attack.mitre.org/mitigations/T1074
- Reviewed: 2026-10-27
