# M1053 Data Backup Outcome Lesson

## Authoritative description

- Technique: **M1053 — Data Backup**

Data Backup involves taking and securely storing backups of data from end-user systems and critical servers. It ensures that data remains available in the event of system compromise, ransomware attacks, or other disruptions. Backup processes should include hardening backup systems, implementing secure storage solutions, and keeping backups isolated from the corporate network to prevent compromise during active incidents. This mitigation can be implemented through the following measures: Regular Backup Scheduling: - Use Case: Ensure timely and consistent backups of critical data. - Implementation: Schedule daily incremental backups and weekly full backups for all critical servers and systems. Immutable Backups: - Use Case: Protect backups from modification or deletion, even by attackers. - Implementation: Use write-once-read-many (WORM) storage for backups, preventing ransomware from encrypting or deleting backup files. Backup Encryption: - Use Case: Protect data integrity and confidentiality during transit and storage. - Implementation: Encrypt backups using strong encryption protocols (e.g., AES-256) before storing them in local, cloud, or remote locations. Offsite Backup Storage: - Use Case: Ensure data availability during physical disasters or onsite breaches. - Implementation: Use cloud-based solutions like AWS S3, Azure Backup, or physical offsite storage to maintain a copy of critical data. Backup Testing: - Use Case: Validate backup integrity and ensure recoverability. - Implementation: Regularly test data restoration processes to ensure that backups are not corrupted and can be recovered quickly.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1053: https://attack.mitre.org/mitigations/M1053
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
