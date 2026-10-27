# Private Keys Technique Response Playbook

## Target technique

**T1552.004 — Private Keys**

- Tactics: credential-access
- Platforms: Linux, macOS, Network Devices, Windows

Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials. Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures. Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. Adversaries may also look in common key directories, such as <code>~/.ssh</code> for SSH keys on * nix-based systems or <code>C:&#92;Users&#92;(username)&#92;.ssh&#92;</code> on Windows. Adversary tools may also search compromised systems for file extensions relating to cryptographic keys and certificates. When a device is registered to Entra ID, a device key and a transport key are generated and used to verify the device’s identity. An adversary with access to the device may be able to export the keys in order to impersonate the device. On network devices, private keys may be exported via Network Device CLI commands such as `crypto pki export`. Some private keys require a password or passphrase for operation, so an adversary may also use Input Capture for keylogging or attempt to Brute Force the passphrase off-line. These private keys can be used to authenticate to Remote Services like SSH or for use in decrypting other collected files such as email.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1552.004: https://attack.mitre.org/techniques/T1552/004
- Reviewed: 2026-10-27
