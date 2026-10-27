# M1047 Audit Outcome Lesson

## Authoritative description

- Technique: **M1047 — Audit**

Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures. Auditing is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver. It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures: System Audit: - Use Case: Regularly assess system configurations to ensure compliance with organizational security policies. - Implementation: Use tools to scan for deviations from established benchmarks. Permission Audits: - Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation. - Implementation: Run access reviews to identify users or groups with excessive permissions. Software Audits: - Use Case: Identify outdated, unsupported, or insecure software that could serve as an attack vector. - Implementation: Use inventory and vulnerability scanning tools to detect outdated versions and recommend secure alternatives. Configuration Audits: - Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA). - Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify non-compliant systems. Network Audits: - Use Case: Examine network traffic, firewall rules, and endpoint communications to identify unauthorized or insecure connections. - Implementation: Utilize tools such as Wireshark, or Zeek to monitor and log suspicious network behavior.

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
- M1047: https://attack.mitre.org/mitigations/M1047
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
