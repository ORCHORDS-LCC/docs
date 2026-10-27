# Password Managers Technique Platform Profile

## Reference

- Technique: **T1555.005 — Password Managers**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may acquire user credentials from third-party password managers. Password managers are applications designed to store user credentials, normally in an encrypted database. Credentials are typically accessible after a user provides a master password that unlocks the database. After the database is unlocked, these credentials may be copied to memory. These databases can be stored as files on disk. Adversaries may acquire user credentials from password managers by extracting the master password and/or plain-text credentials from memory. Adversaries may extract credentials from memory via Exploitation for Credential Access. Adversaries may also try brute forcing via Password Guessing to obtain the master password of a password manager.

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
- T1555.005: https://attack.mitre.org/techniques/T1555/005
- Reviewed: 2026-10-27
