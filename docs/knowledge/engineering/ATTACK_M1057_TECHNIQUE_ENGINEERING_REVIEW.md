# Data Loss Prevention Technique Engineering Review

## Reference

- Technique: **M1057 — Data Loss Prevention**

Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. This mitigation can be implemented through the following measures: Sensitive Data Categorization: - Use Case: Identify and classify data based on sensitivity (e.g., PII, financial data, trade secrets). - Implementation: Use DLP solutions to scan and tag files containing sensitive information using predefined patterns, such as Social Security Numbers or credit card details. Exfiltration Restrictions: - Use Case: Prevent unauthorized transmission of sensitive data. - Implementation: Enforce policies to block unapproved email attachments, unauthorized USB usage, or unencrypted data uploads to cloud storage. Data-in-Transit Monitoring: - Use Case: Detect and prevent the transmission of sensitive data over unapproved channels. - Implementation: Deploy network-based DLP tools to inspect outbound traffic for sensitive content (e.g., financial records or PII) and block unapproved transmissions. Endpoint Data Protection: - Use Case: Monitor and control sensitive data usage on endpoints. - Implementation: Use endpoint-based DLP agents to block copy-paste actions of sensitive data and unauthorized printing or file sharing. Cloud Data Security: - Use Case: Protect data stored in cloud platforms. - Implementation: Integrate DLP with cloud storage platforms like Google Drive, OneDrive, or AWS to monitor and restrict sensitive data sharing or downloads.

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
- M1057: https://attack.mitre.org/mitigations/M1057
- Reviewed: 2026-10-27
