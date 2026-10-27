# Filter Network Traffic Technique Platform Profile

## Reference

- Technique: **M1037 — Filter Network Traffic**
- Platforms named in the source: not stated

Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures: Ingress Traffic Filtering: - Use Case: Configure network firewalls to allow traffic only from authorized IP addresses to public-facing servers. - Implementation: Limit SSH (port 22) and RDP (port 3389) traffic to specific IP ranges. Egress Traffic Filtering: - Use Case: Use firewalls or endpoint security software to block unauthorized outbound traffic to prevent data exfiltration and command-and-control (C2) communications. - Implementation: Block outbound traffic to known malicious IPs or regions where communication is unexpected. Protocol-Based Filtering: - Use Case: Restrict the use of specific protocols that are commonly abused by adversaries, such as SMB, RPC, or Telnet, based on business needs. - Implementation: Disable SMBv1 on endpoints to prevent exploits like EternalBlue. Network Segmentation: - Use Case: Create network segments for critical systems and restrict communication between segments unless explicitly authorized. - Implementation: Implement VLANs to isolate IoT devices or guest networks from core business systems. Application Layer Filtering: - Use Case: Use proxy servers or Web Application Firewalls (WAFs) to inspect and block malicious HTTP/S traffic. - Implementation: Configure a WAF to block SQL injection attempts or other web application exploitation techniques.

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
- M1037: https://attack.mitre.org/mitigations/M1037
- Reviewed: 2026-10-27
