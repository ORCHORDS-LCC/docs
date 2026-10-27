# Private Keys Technique Platform Profile

## Reference

- Technique: **T1552.004 — Private Keys**
- Platforms named in the source: Linux, macOS, Network Devices, Windows

Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials. Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures. Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. Adversaries may also look in common key directories, such as <code>~/.ssh</code> for SSH keys on * nix-based systems or <code>C:&#92;Users&#92;(username)&#92;.ssh&#92;</code> on Windows. Adversary tools may also search compromised systems for file extensions relating to cryptographic keys and certificates. When a device is registered to Entra ID, a device key and a transport key are generated and used to verify the device’s identity. An adversary with access to the device may be able to export the keys in order to impersonate the device. On network devices, private keys may be exported via Network Device CLI commands such as `crypto pki export`. Some private keys require a password or passphrase for operation, so an adversary may also use Input Capture for keylogging or attempt to Brute Force the passphrase off-line. These private keys can be used to authenticate to Remote Services like SSH or for use in decrypting other collected files such as email.

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
- T1552.004: https://attack.mitre.org/techniques/T1552/004
- Reviewed: 2026-10-27
