# Data Backup Technique Response Playbook

## Target technique

**M1053 — Data Backup**


Data Backup involves taking and securely storing backups of data from end-user systems and critical servers. It ensures that data remains available in the event of system compromise, ransomware attacks, or other disruptions. Backup processes should include hardening backup systems, implementing secure storage solutions, and keeping backups isolated from the corporate network to prevent compromise during active incidents. This mitigation can be implemented through the following measures: Regular Backup Scheduling: - Use Case: Ensure timely and consistent backups of critical data. - Implementation: Schedule daily incremental backups and weekly full backups for all critical servers and systems. Immutable Backups: - Use Case: Protect backups from modification or deletion, even by attackers. - Implementation: Use write-once-read-many (WORM) storage for backups, preventing ransomware from encrypting or deleting backup files. Backup Encryption: - Use Case: Protect data integrity and confidentiality during transit and storage. - Implementation: Encrypt backups using strong encryption protocols (e.g., AES-256) before storing them in local, cloud, or remote locations. Offsite Backup Storage: - Use Case: Ensure data availability during physical disasters or onsite breaches. - Implementation: Use cloud-based solutions like AWS S3, Azure Backup, or physical offsite storage to maintain a copy of critical data. Backup Testing: - Use Case: Validate backup integrity and ensure recoverability. - Implementation: Regularly test data restoration processes to ensure that backups are not corrupted and can be recovered quickly.

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
- M1053: https://attack.mitre.org/mitigations/M1053
- Reviewed: 2026-10-27
