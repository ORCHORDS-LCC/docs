# Network Traffic Content Technique Operationalization Review

## Reference

- Technique: **DC0085 — Network Traffic Content**

The full packet capture (PCAP) or session data that logs both protocol headers and payload content. This allows analysts to inspect command and control (C2) traffic, exfiltration, and other suspicious activity within network communications. Unlike metadata-based logs, full content analysis enables deeper protocol inspection, payload decoding, and forensic investigations. *Data Collection Measures:* - Network Packet Capture (Full Content Logging) - Wireshark / tcpdump / tshark - Full packet captures (PCAP files) for manual analysis or IDS correlation. `tcpdump -i eth0 -w capture.pcap` - Zeek (formerly Bro) - Extracts protocol headers and payload details into structured logs. `echo "redef Log::default_store = Log::ASCII;" > local.zeek | zeek -Cr capture.pcap local.zeek` - Suricata / Snort (IDS/IPS with PCAP Logging) - Deep packet inspection (DPI) with signature-based and behavioral analysis. `suricata -c /etc/suricata/suricata.yaml -i eth0 -l /var/log/suricata` - Host-Based Collection - Sysmon Event ID 22 – DNS Query Logging, Captures DNS requests made by processes, useful for detecting C2 domains. - Sysmon Event ID 3 – Network Connection Initiated, Logs process-to-network connection relationships. - AuditD (Linux) – syscall=connect, Monitors outbound network requests from processes. `auditctl -a always,exit -F arch=b64 -S connect -k network_activity` - Cloud & SaaS Traffic Collection - AWS VPC Flow Logs / Azure NSG Flow Logs / Google VPC Flow Logs, Captures metadata about inbound/outbound network traffic. - Cloud IDS (AWS GuardDuty, Azure Sentinel, Google Chronicle), Detects malicious activity in cloud environments by analyzing network traffic patterns.

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
- DC0085: https://attack.mitre.org/datacomponents/DC0085
- Reviewed: 2026-10-27
