# Private Keys Technique Engineering Review

## Reference

- Technique: **T1552.004 — Private Keys**

Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials. Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures. Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. Adversaries may also look in common key directories, such as ~/.ssh for SSH keys on * nix-based systems or C:&#92;Users&#92;(username)&#92;.ssh&#92; on Windows. Adversary tools may also search compromised systems for file extensions relating to cryptographic keys and certificates. When a device is registered to Entra ID, a device key and a transport key are generated and used to verify the device’s identity. An adversary with access to the device may be able to export the keys in order to impersonate the device. On network devices, private keys may be exported via Network Device CLI commands such as `crypto pki export`. Some private keys require a password or passphrase for operation, so an adversary may also use Input Capture for keylogging or attempt to Brute Force the passphrase off-line. These private keys can be used to authenticate to Remote Services like SSH or for use in decrypting other collected files such as email.

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
- T1552.004: https://attack.mitre.org/techniques/T1552/004
- Reviewed: 2026-10-27
