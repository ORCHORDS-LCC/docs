# Network Traffic Content Technique Platform Profile

## Reference

- Technique: **DC0085 — Network Traffic Content**
- Platforms named in the source: not stated

The full packet capture (PCAP) or session data that logs both protocol headers and payload content. This allows analysts to inspect command and control (C2) traffic, exfiltration, and other suspicious activity within network communications. Unlike metadata-based logs, full content analysis enables deeper protocol inspection, payload decoding, and forensic investigations. *Data Collection Measures:* - Network Packet Capture (Full Content Logging) - Wireshark / tcpdump / tshark - Full packet captures (PCAP files) for manual analysis or IDS correlation. `tcpdump -i eth0 -w capture.pcap` - Zeek (formerly Bro) - Extracts protocol headers and payload details into structured logs. `echo "redef Log::default_store = Log::ASCII;" > local.zeek | zeek -Cr capture.pcap local.zeek` - Suricata / Snort (IDS/IPS with PCAP Logging) - Deep packet inspection (DPI) with signature-based and behavioral analysis. `suricata -c /etc/suricata/suricata.yaml -i eth0 -l /var/log/suricata` - Host-Based Collection - Sysmon Event ID 22 – DNS Query Logging, Captures DNS requests made by processes, useful for detecting C2 domains. - Sysmon Event ID 3 – Network Connection Initiated, Logs process-to-network connection relationships. - AuditD (Linux) – syscall=connect, Monitors outbound network requests from processes. `auditctl -a always,exit -F arch=b64 -S connect -k network_activity` - Cloud & SaaS Traffic Collection - AWS VPC Flow Logs / Azure NSG Flow Logs / Google VPC Flow Logs, Captures metadata about inbound/outbound network traffic. - Cloud IDS (AWS GuardDuty, Azure Sentinel, Google Chronicle), Detects malicious activity in cloud environments by analyzing network traffic patterns.

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
- DC0085: https://attack.mitre.org/datacomponents/DC0085
- Reviewed: 2026-10-27
