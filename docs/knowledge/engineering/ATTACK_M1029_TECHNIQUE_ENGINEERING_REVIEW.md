# Remote Data Storage Technique Engineering Review

## Reference

- Technique: **M1029 — Remote Data Storage**

Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures: Centralized Log Management: - Configure endpoints to forward security logs to a centralized log collector or SIEM. - Use tools like Splunk Graylog, or Security Onion to aggregate and store logs. - Example command (Linux): `sudo auditd | tee /var/log/audit/audit.log | nc <remote-log-server> 514` Remote File Storage Solutions: - Utilize cloud storage solutions like AWS S3, Google Cloud Storage, or Azure Blob Storage for sensitive data. - Ensure proper encryption at rest and access control policies (IAM roles, ACLs). Intrusion Detection Log Forwarding: - Forward logs from IDS/IPS systems (e.g., Zeek/Suricata) to a remote security information system. - Example for Suricata log forwarding: `outputs: - type: syslog protocol: tls address: <remote-syslog-server>` Immutable Backup Configurations: - Enable immutable storage settings for backups to prevent adversaries from modifying or deleting data. - Example: AWS S3 Object Lock. Data Encryption: - Ensure encryption for sensitive data using AES-256 at rest and TLS 1.2+ for data in transit. Tools: OpenSSL, BitLocker, LUKS for Linux.

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
- M1029: https://attack.mitre.org/mitigations/M1029
- Reviewed: 2026-10-27
