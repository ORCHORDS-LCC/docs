# Filter Network Traffic Technique Response Playbook

## Target technique

**M1037 — Filter Network Traffic**


Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures: Ingress Traffic Filtering: - Use Case: Configure network firewalls to allow traffic only from authorized IP addresses to public-facing servers. - Implementation: Limit SSH (port 22) and RDP (port 3389) traffic to specific IP ranges. Egress Traffic Filtering: - Use Case: Use firewalls or endpoint security software to block unauthorized outbound traffic to prevent data exfiltration and command-and-control (C2) communications. - Implementation: Block outbound traffic to known malicious IPs or regions where communication is unexpected. Protocol-Based Filtering: - Use Case: Restrict the use of specific protocols that are commonly abused by adversaries, such as SMB, RPC, or Telnet, based on business needs. - Implementation: Disable SMBv1 on endpoints to prevent exploits like EternalBlue. Network Segmentation: - Use Case: Create network segments for critical systems and restrict communication between segments unless explicitly authorized. - Implementation: Implement VLANs to isolate IoT devices or guest networks from core business systems. Application Layer Filtering: - Use Case: Use proxy servers or Web Application Firewalls (WAFs) to inspect and block malicious HTTP/S traffic. - Implementation: Configure a WAF to block SQL injection attempts or other web application exploitation techniques.

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
- M1037: https://attack.mitre.org/mitigations/M1037
- Reviewed: 2026-10-27
