# T1555.002 Securityd Memory Outcome Lesson

## Authoritative description

- Technique: **T1555.002 — Securityd Memory**
- Tactics: credential-access
- Platforms: Linux, macOS

An adversary with root access may gather credentials by reading `securityd`’s memory. `securityd` is a service/daemon responsible for implementing security protocols such as encryption and authorization. A privileged adversary may be able to scan through `securityd`'s memory to find the correct sequence of keys to decrypt the user’s logon keychain. This may provide the adversary with various plaintext passwords, such as those for users, WiFi, mail, browsers, certificates, secure notes, etc. In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords. Apple’s `securityd` utility takes the user’s logon password, encrypts it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s password, but once the master key is found, an adversary need only iterate over the other values to unlock the final password.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1555.002: https://attack.mitre.org/techniques/T1555/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
