# Steal or Forge Authentication Certificates Technique Operationalization Review

## Reference

- Technique: **T1649 — Steal or Forge Authentication Certificates**

Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material. For example, Entra ID device certificates and Active Directory Certificate Services (AD CS) certificates bind to an identity and can be used as credentials for domain accounts. Authentication certificates can be both stolen and forged. For example, AD CS certificates can be stolen from encrypted storage (in the Registry or files), misplaced certificate files (i.e. Unsecured Credentials), or directly from the Windows certificate store via various crypto APIs. With appropriate enrollment rights, users and/or machines within a domain can also request and/or manually renew certificates from enterprise certificate authorities (CA). This enrollment process defines various settings and permissions associated with the certificate. Of note, the certificate’s extended key usage (EKU) values define signing, encryption, and authentication use cases, while the certificate’s subject alternative name (SAN) values define the certificate owner’s alternate names. Abusing certificates for authentication credentials may enable other behaviors such as Lateral Movement. Certificate-related misconfigurations may also enable opportunities for Privilege Escalation, by way of allowing users to impersonate or assume privileged accounts or permissions via the identities (SANs) associated with a certificate. These abuses may also enable Persistence via stealing or forging certificates that can be used as Valid Accounts for the duration of the certificate's validity, despite user password resets. Authentication certificates can also be stolen and forged for machine accounts. Adversaries who have access to root (or subordinate) CA certificate private keys (or mechanisms protecting/managing these keys) may also establish Persistence by forging arbitrary authentication certificates for the victim domain (known as “golden” certificates). Adversaries may also target certificates and related services in order to access other forms of credentials, such as Golden Ticket ticket-granting tickets (TGT) or NTLM plaintext.

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
- T1649: https://attack.mitre.org/techniques/T1649
- Reviewed: 2026-10-27
