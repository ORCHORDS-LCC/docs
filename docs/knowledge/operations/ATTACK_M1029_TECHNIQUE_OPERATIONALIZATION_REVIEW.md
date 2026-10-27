# Remote Data Storage Technique Operationalization Review

## Reference

- Technique: **M1029 — Remote Data Storage**

Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures: Centralized Log Management: - Configure endpoints to forward security logs to a centralized log collector or SIEM. - Use tools like Splunk Graylog, or Security Onion to aggregate and store logs. - Example command (Linux): `sudo auditd | tee /var/log/audit/audit.log | nc <remote-log-server> 514` Remote File Storage Solutions: - Utilize cloud storage solutions like AWS S3, Google Cloud Storage, or Azure Blob Storage for sensitive data. - Ensure proper encryption at rest and access control policies (IAM roles, ACLs). Intrusion Detection Log Forwarding: - Forward logs from IDS/IPS systems (e.g., Zeek/Suricata) to a remote security information system. - Example for Suricata log forwarding: `outputs: - type: syslog protocol: tls address: <remote-syslog-server>` Immutable Backup Configurations: - Enable immutable storage settings for backups to prevent adversaries from modifying or deleting data. - Example: AWS S3 Object Lock. Data Encryption: - Ensure encryption for sensitive data using AES-256 at rest and TLS 1.2+ for data in transit. Tools: OpenSSL, BitLocker, LUKS for Linux.

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
- M1029: https://attack.mitre.org/mitigations/M1029
- Reviewed: 2026-10-27
