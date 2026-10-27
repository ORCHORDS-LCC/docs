# Audit Technique Response Playbook

## Target technique

**M1047 — Audit**


Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures. Auditing is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver. It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures: System Audit: - Use Case: Regularly assess system configurations to ensure compliance with organizational security policies. - Implementation: Use tools to scan for deviations from established benchmarks. Permission Audits: - Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation. - Implementation: Run access reviews to identify users or groups with excessive permissions. Software Audits: - Use Case: Identify outdated, unsupported, or insecure software that could serve as an attack vector. - Implementation: Use inventory and vulnerability scanning tools to detect outdated versions and recommend secure alternatives. Configuration Audits: - Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA). - Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify non-compliant systems. Network Audits: - Use Case: Examine network traffic, firewall rules, and endpoint communications to identify unauthorized or insecure connections. - Implementation: Utilize tools such as Wireshark, or Zeek to monitor and log suspicious network behavior.

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
- M1047: https://attack.mitre.org/mitigations/M1047
- Reviewed: 2026-10-27
