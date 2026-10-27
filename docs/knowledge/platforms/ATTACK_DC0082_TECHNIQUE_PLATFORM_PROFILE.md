# Network Connection Creation Technique Platform Profile

## Reference

- Technique: **DC0082 — Network Connection Creation**
- Platforms named in the source: not stated

The initial establishment of a network session, where a system or process initiates a connection to a local or remote endpoint. This typically involves capturing socket information (source/destination IP, ports, protocol) and tracking session metadata. Monitoring these events helps detect lateral movement, exfiltration, and command-and-control (C2) activities. *Data Collection Measures:* - Windows: - Event ID 5156 – Filtering Platform Connection - Logs network connections permitted by Windows Filtering Platform (WFP). - Sysmon Event ID 3 – Network Connection Initiated - Captures process, source/destination IP, ports, and parent process. - Linux/macOS: - Netfilter (iptables), nftables logs - Tracks incoming and outgoing network connections. - AuditD (`connect` syscall) - Logs TCP, UDP, and ICMP connections. - Zeek (`conn.log`) - Captures protocol, duration, and bytes transferred. - Cloud & Network Infrastructure: - AWS VPC Flow Logs / Azure NSG Flow Logs - Logs IP traffic at the network level in cloud environments. - Zeek (conn.log) or Suricata (network events) - Captures packet metadata for detection and correlation. - Endpoint Detection & Response (EDR): - Detect anomalous network activity such as new C2 connections or data exfiltration attempts.

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
- DC0082: https://attack.mitre.org/datacomponents/DC0082
- Reviewed: 2026-10-27
