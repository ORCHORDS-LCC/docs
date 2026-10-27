# Data Loss Prevention Technique Operationalization Review

## Reference

- Technique: **M1057 — Data Loss Prevention**

Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. This mitigation can be implemented through the following measures: Sensitive Data Categorization: - Use Case: Identify and classify data based on sensitivity (e.g., PII, financial data, trade secrets). - Implementation: Use DLP solutions to scan and tag files containing sensitive information using predefined patterns, such as Social Security Numbers or credit card details. Exfiltration Restrictions: - Use Case: Prevent unauthorized transmission of sensitive data. - Implementation: Enforce policies to block unapproved email attachments, unauthorized USB usage, or unencrypted data uploads to cloud storage. Data-in-Transit Monitoring: - Use Case: Detect and prevent the transmission of sensitive data over unapproved channels. - Implementation: Deploy network-based DLP tools to inspect outbound traffic for sensitive content (e.g., financial records or PII) and block unapproved transmissions. Endpoint Data Protection: - Use Case: Monitor and control sensitive data usage on endpoints. - Implementation: Use endpoint-based DLP agents to block copy-paste actions of sensitive data and unauthorized printing or file sharing. Cloud Data Security: - Use Case: Protect data stored in cloud platforms. - Implementation: Integrate DLP with cloud storage platforms like Google Drive, OneDrive, or AWS to monitor and restrict sensitive data sharing or downloads.

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
- M1057: https://attack.mitre.org/mitigations/M1057
- Reviewed: 2026-10-27
