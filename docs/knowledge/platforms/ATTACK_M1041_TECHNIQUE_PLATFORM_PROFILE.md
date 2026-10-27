# Encrypt Sensitive Information Technique Platform Profile

## Reference

- Technique: **M1041 — Encrypt Sensitive Information**
- Platforms named in the source: not stated

Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures: Encrypt Data at Rest: - Use Case: Use full-disk encryption or file-level encryption to secure sensitive data stored on devices. - Implementation: Implement BitLocker for Windows systems or FileVault for macOS devices to encrypt hard drives. Encrypt Data in Transit: - Use Case: Use secure communication protocols (e.g., TLS, HTTPS) to encrypt sensitive data as it travels over networks. - Implementation: Enable HTTPS for all web applications and configure mail servers to enforce STARTTLS for email encryption. Encrypt Backups: - Use Case: Ensure that backup data is encrypted both during storage and transfer to prevent unauthorized access. - Implementation: Encrypt cloud backups using AES-256 before uploading them to Amazon S3 or Google Cloud. Encrypt Application Secrets: - Use Case: Store sensitive credentials, API keys, and configuration files in encrypted vaults. - Implementation: Use HashiCorp Vault or AWS Secrets Manager to manage and encrypt secrets. Database Encryption: - Use Case: Enable Transparent Data Encryption (TDE) or column-level encryption in database management systems. - Implementation: Use MySQL’s built-in encryption features to encrypt sensitive database fields such as social security numbers.

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
- M1041: https://attack.mitre.org/mitigations/M1041
- Reviewed: 2026-10-27
