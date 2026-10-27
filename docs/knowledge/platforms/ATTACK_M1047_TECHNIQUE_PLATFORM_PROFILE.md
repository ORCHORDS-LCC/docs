# Audit Technique Platform Profile

## Reference

- Technique: **M1047 — Audit**
- Platforms named in the source: not stated

Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures. Auditing is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver. It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures: System Audit: - Use Case: Regularly assess system configurations to ensure compliance with organizational security policies. - Implementation: Use tools to scan for deviations from established benchmarks. Permission Audits: - Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation. - Implementation: Run access reviews to identify users or groups with excessive permissions. Software Audits: - Use Case: Identify outdated, unsupported, or insecure software that could serve as an attack vector. - Implementation: Use inventory and vulnerability scanning tools to detect outdated versions and recommend secure alternatives. Configuration Audits: - Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA). - Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify non-compliant systems. Network Audits: - Use Case: Examine network traffic, firewall rules, and endpoint communications to identify unauthorized or insecure connections. - Implementation: Utilize tools such as Wireshark, or Zeek to monitor and log suspicious network behavior.

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
- M1047: https://attack.mitre.org/mitigations/M1047
- Reviewed: 2026-10-27
