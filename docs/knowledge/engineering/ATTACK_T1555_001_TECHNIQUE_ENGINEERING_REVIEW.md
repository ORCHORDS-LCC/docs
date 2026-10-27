# Keychain Technique Engineering Review

## Reference

- Technique: **T1555.001 — Keychain**

Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and secure notes. There are three types of Keychains: Login Keychain, System Keychain, and Local Items (iCloud) Keychain. The default Keychain is the Login Keychain, which stores user passwords and information. The System Keychain stores items accessed by the operating system, such as items shared among users on a host. The Local Items (iCloud) Keychain is used for items synced with Apple’s iCloud service. Keychains can be viewed and edited through the Keychain Access application or using the command-line utility security. Keychain files are located in ~/Library/Keychains/, /Library/Keychains/, and /Network/Library/Keychains/. Adversaries may gather user credentials from Keychain storage/memory. For example, the command security dump-keychain –d will dump all Login Keychain credentials from ~/Library/Keychains/login.keychain-db. Adversaries may also directly read Login Keychain credentials from the ~/Library/Keychains/login.keychain file. Both methods require a password, where the default password for the Login Keychain is the current user’s password to login to the macOS host.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1555.001: https://attack.mitre.org/techniques/T1555/001
- Reviewed: 2026-10-27
