# Keychain Technique Operationalization Review

## Reference

- Technique: **T1555.001 — Keychain**

Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and secure notes. There are three types of Keychains: Login Keychain, System Keychain, and Local Items (iCloud) Keychain. The default Keychain is the Login Keychain, which stores user passwords and information. The System Keychain stores items accessed by the operating system, such as items shared among users on a host. The Local Items (iCloud) Keychain is used for items synced with Apple’s iCloud service. Keychains can be viewed and edited through the Keychain Access application or using the command-line utility security. Keychain files are located in ~/Library/Keychains/, /Library/Keychains/, and /Network/Library/Keychains/. Adversaries may gather user credentials from Keychain storage/memory. For example, the command security dump-keychain –d will dump all Login Keychain credentials from ~/Library/Keychains/login.keychain-db. Adversaries may also directly read Login Keychain credentials from the ~/Library/Keychains/login.keychain file. Both methods require a password, where the default password for the Login Keychain is the current user’s password to login to the macOS host.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1555.001: https://attack.mitre.org/techniques/T1555/001
- Reviewed: 2026-10-27
