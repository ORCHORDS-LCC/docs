# Remote Data Storage Technique Response Playbook

## Target technique

**M1029 — Remote Data Storage**


Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures: Centralized Log Management: - Configure endpoints to forward security logs to a centralized log collector or SIEM. - Use tools like Splunk Graylog, or Security Onion to aggregate and store logs. - Example command (Linux): `sudo auditd | tee /var/log/audit/audit.log | nc <remote-log-server> 514` Remote File Storage Solutions: - Utilize cloud storage solutions like AWS S3, Google Cloud Storage, or Azure Blob Storage for sensitive data. - Ensure proper encryption at rest and access control policies (IAM roles, ACLs). Intrusion Detection Log Forwarding: - Forward logs from IDS/IPS systems (e.g., Zeek/Suricata) to a remote security information system. - Example for Suricata log forwarding: `outputs: - type: syslog protocol: tls address: <remote-syslog-server>` Immutable Backup Configurations: - Enable immutable storage settings for backups to prevent adversaries from modifying or deleting data. - Example: AWS S3 Object Lock. Data Encryption: - Ensure encryption for sensitive data using AES-256 at rest and TLS 1.2+ for data in transit. Tools: OpenSSL, BitLocker, LUKS for Linux.

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
- M1029: https://attack.mitre.org/mitigations/M1029
- Reviewed: 2026-10-27
