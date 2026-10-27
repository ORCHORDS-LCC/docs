# Encrypt Sensitive Information Technique Response Playbook

## Target technique

**M1041 — Encrypt Sensitive Information**


Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures: Encrypt Data at Rest: - Use Case: Use full-disk encryption or file-level encryption to secure sensitive data stored on devices. - Implementation: Implement BitLocker for Windows systems or FileVault for macOS devices to encrypt hard drives. Encrypt Data in Transit: - Use Case: Use secure communication protocols (e.g., TLS, HTTPS) to encrypt sensitive data as it travels over networks. - Implementation: Enable HTTPS for all web applications and configure mail servers to enforce STARTTLS for email encryption. Encrypt Backups: - Use Case: Ensure that backup data is encrypted both during storage and transfer to prevent unauthorized access. - Implementation: Encrypt cloud backups using AES-256 before uploading them to Amazon S3 or Google Cloud. Encrypt Application Secrets: - Use Case: Store sensitive credentials, API keys, and configuration files in encrypted vaults. - Implementation: Use HashiCorp Vault or AWS Secrets Manager to manage and encrypt secrets. Database Encryption: - Use Case: Enable Transparent Data Encryption (TDE) or column-level encryption in database management systems. - Implementation: Use MySQL’s built-in encryption features to encrypt sensitive database fields such as social security numbers.

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
- M1041: https://attack.mitre.org/mitigations/M1041
- Reviewed: 2026-10-27
