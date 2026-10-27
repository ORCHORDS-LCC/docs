# Data Loss Prevention Technique Platform Profile

## Reference

- Technique: **M1057 — Data Loss Prevention**
- Platforms named in the source: not stated

Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. This mitigation can be implemented through the following measures: Sensitive Data Categorization: - Use Case: Identify and classify data based on sensitivity (e.g., PII, financial data, trade secrets). - Implementation: Use DLP solutions to scan and tag files containing sensitive information using predefined patterns, such as Social Security Numbers or credit card details. Exfiltration Restrictions: - Use Case: Prevent unauthorized transmission of sensitive data. - Implementation: Enforce policies to block unapproved email attachments, unauthorized USB usage, or unencrypted data uploads to cloud storage. Data-in-Transit Monitoring: - Use Case: Detect and prevent the transmission of sensitive data over unapproved channels. - Implementation: Deploy network-based DLP tools to inspect outbound traffic for sensitive content (e.g., financial records or PII) and block unapproved transmissions. Endpoint Data Protection: - Use Case: Monitor and control sensitive data usage on endpoints. - Implementation: Use endpoint-based DLP agents to block copy-paste actions of sensitive data and unauthorized printing or file sharing. Cloud Data Security: - Use Case: Protect data stored in cloud platforms. - Implementation: Integrate DLP with cloud storage platforms like Google Drive, OneDrive, or AWS to monitor and restrict sensitive data sharing or downloads.

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
- M1057: https://attack.mitre.org/mitigations/M1057
- Reviewed: 2026-10-27
