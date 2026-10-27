# Steal or Forge Authentication Certificates Technique Response Playbook

## Target technique

**T1649 — Steal or Forge Authentication Certificates**

- Tactics: credential-access
- Platforms: Windows, Linux, macOS, Identity Provider

Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material. For example, Entra ID device certificates and Active Directory Certificate Services (AD CS) certificates bind to an identity and can be used as credentials for domain accounts. Authentication certificates can be both stolen and forged. For example, AD CS certificates can be stolen from encrypted storage (in the Registry or files), misplaced certificate files (i.e. Unsecured Credentials), or directly from the Windows certificate store via various crypto APIs. With appropriate enrollment rights, users and/or machines within a domain can also request and/or manually renew certificates from enterprise certificate authorities (CA). This enrollment process defines various settings and permissions associated with the certificate. Of note, the certificate’s extended key usage (EKU) values define signing, encryption, and authentication use cases, while the certificate’s subject alternative name (SAN) values define the certificate owner’s alternate names. Abusing certificates for authentication credentials may enable other behaviors such as Lateral Movement. Certificate-related misconfigurations may also enable opportunities for Privilege Escalation, by way of allowing users to impersonate or assume privileged accounts or permissions via the identities (SANs) associated with a certificate. These abuses may also enable Persistence via stealing or forging certificates that can be used as Valid Accounts for the duration of the certificate's validity, despite user password resets. Authentication certificates can also be stolen and forged for machine accounts. Adversaries who have access to root (or subordinate) CA certificate private keys (or mechanisms protecting/managing these keys) may also establish Persistence by forging arbitrary authentication certificates for the victim domain (known as “golden” certificates). Adversaries may also target certificates and related services in order to access other forms of credentials, such as Golden Ticket ticket-granting tickets (TGT) or NTLM plaintext.

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
- T1649: https://attack.mitre.org/techniques/T1649
- Reviewed: 2026-10-27
