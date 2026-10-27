# Credentials In Files Technique Platform Profile

## Reference

- Technique: **T1552.001 — Credentials In Files**
- Platforms named in the source: Containers, IaaS, Linux, macOS, Windows

Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords. It is possible to extract passwords from backups or saved virtual machines through OS Credential Dumping. Passwords may also be obtained from Group Policy Preferences stored on the Windows Domain Controller. In cloud and/or containerized environments, authenticated user and service account credentials are often stored in local configuration and credential files. They may also be found as parameters to deployment commands in container logs. In some cases, these files can be copied and reused on another machine or the contents can be read and then used to authenticate without needing to copy any files.

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
- T1552.001: https://attack.mitre.org/techniques/T1552/001
- Reviewed: 2026-10-27
