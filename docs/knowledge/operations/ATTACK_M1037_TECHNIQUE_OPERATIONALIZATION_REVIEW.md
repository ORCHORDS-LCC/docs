# Filter Network Traffic Technique Operationalization Review

## Reference

- Technique: **M1037 — Filter Network Traffic**

Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures: Ingress Traffic Filtering: - Use Case: Configure network firewalls to allow traffic only from authorized IP addresses to public-facing servers. - Implementation: Limit SSH (port 22) and RDP (port 3389) traffic to specific IP ranges. Egress Traffic Filtering: - Use Case: Use firewalls or endpoint security software to block unauthorized outbound traffic to prevent data exfiltration and command-and-control (C2) communications. - Implementation: Block outbound traffic to known malicious IPs or regions where communication is unexpected. Protocol-Based Filtering: - Use Case: Restrict the use of specific protocols that are commonly abused by adversaries, such as SMB, RPC, or Telnet, based on business needs. - Implementation: Disable SMBv1 on endpoints to prevent exploits like EternalBlue. Network Segmentation: - Use Case: Create network segments for critical systems and restrict communication between segments unless explicitly authorized. - Implementation: Implement VLANs to isolate IoT devices or guest networks from core business systems. Application Layer Filtering: - Use Case: Use proxy servers or Web Application Firewalls (WAFs) to inspect and block malicious HTTP/S traffic. - Implementation: Configure a WAF to block SQL injection attempts or other web application exploitation techniques.

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
- M1037: https://attack.mitre.org/mitigations/M1037
- Reviewed: 2026-10-27
