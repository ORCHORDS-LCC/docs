# Keychain Technique Platform Profile

## Reference

- Technique: **T1555.001 — Keychain**
- Platforms named in the source: macOS

Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and secure notes. There are three types of Keychains: Login Keychain, System Keychain, and Local Items (iCloud) Keychain. The default Keychain is the Login Keychain, which stores user passwords and information. The System Keychain stores items accessed by the operating system, such as items shared among users on a host. The Local Items (iCloud) Keychain is used for items synced with Apple’s iCloud service. Keychains can be viewed and edited through the Keychain Access application or using the command-line utility security. Keychain files are located in ~/Library/Keychains/, /Library/Keychains/, and /Network/Library/Keychains/. Adversaries may gather user credentials from Keychain storage/memory. For example, the command security dump-keychain –d will dump all Login Keychain credentials from ~/Library/Keychains/login.keychain-db. Adversaries may also directly read Login Keychain credentials from the ~/Library/Keychains/login.keychain file. Both methods require a password, where the default password for the Login Keychain is the current user’s password to login to the macOS host.

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
- T1555.001: https://attack.mitre.org/techniques/T1555/001
- Reviewed: 2026-10-27
