# T1145 Private Keys Outcome Lesson

## Authoritative description

- Technique: **T1145 — Private Keys**
- Tactics: credential-access
- Platforms: Linux, macOS, Windows

Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures. Adversaries may gather private keys from compromised systems for use in authenticating to Remote Services like SSH or for use in decrypting other collected files such as email. Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. Adversaries may also look in common key directories, such as ~/.ssh for SSH keys on * nix-based systems or (a user home directory).ssh\ on Windows. Private keys should require a password or passphrase for operation, so an adversary may also use Input Capture for keylogging or attempt to Brute Force the passphrase off-line. Adversary tools have been discovered that search compromised systems for file extensions relating to cryptographic keys and certificates.

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
- T1145: https://attack.mitre.org/techniques/T1145
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
