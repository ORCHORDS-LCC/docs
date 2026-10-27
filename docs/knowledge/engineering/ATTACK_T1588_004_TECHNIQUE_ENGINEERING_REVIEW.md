# Digital Certificates Technique Engineering Review

## Reference

- Technique: **T1588.004 — Digital Certificates**

Adversaries may buy and/or steal SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner. Adversaries may purchase or steal SSL/TLS certificates to further their operations, such as encrypting C2 traffic (ex: Asymmetric Cryptography with Web Protocols) or even enabling Adversary-in-the-Middle if the certificate is trusted or otherwise added to the root of trust (i.e. Install Root Certificate). The purchase of digital certificates may be done using a front organization or using information stolen from a previously compromised entity that allows the adversary to validate to a certificate provider as that entity. Adversaries may also steal certificate materials directly from a compromised third-party, including from certificate authorities. Adversaries may register or hijack domains that they will later purchase an SSL/TLS certificate for. Certificate authorities exist that allow adversaries to acquire SSL/TLS certificates, such as domain validation certificates, for free. After obtaining a digital certificate, an adversary may then install that certificate (see Install Digital Certificate) on infrastructure under their control.

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
- T1588.004: https://attack.mitre.org/techniques/T1588/004
- Reviewed: 2026-10-27
