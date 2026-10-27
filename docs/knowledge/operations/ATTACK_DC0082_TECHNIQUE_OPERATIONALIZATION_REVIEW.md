# Network Connection Creation Technique Operationalization Review

## Reference

- Technique: **DC0082 — Network Connection Creation**

The initial establishment of a network session, where a system or process initiates a connection to a local or remote endpoint. This typically involves capturing socket information (source/destination IP, ports, protocol) and tracking session metadata. Monitoring these events helps detect lateral movement, exfiltration, and command-and-control (C2) activities. *Data Collection Measures:* - Windows: - Event ID 5156 – Filtering Platform Connection - Logs network connections permitted by Windows Filtering Platform (WFP). - Sysmon Event ID 3 – Network Connection Initiated - Captures process, source/destination IP, ports, and parent process. - Linux/macOS: - Netfilter (iptables), nftables logs - Tracks incoming and outgoing network connections. - AuditD (`connect` syscall) - Logs TCP, UDP, and ICMP connections. - Zeek (`conn.log`) - Captures protocol, duration, and bytes transferred. - Cloud & Network Infrastructure: - AWS VPC Flow Logs / Azure NSG Flow Logs - Logs IP traffic at the network level in cloud environments. - Zeek (conn.log) or Suricata (network events) - Captures packet metadata for detection and correlation. - Endpoint Detection & Response (EDR): - Detect anomalous network activity such as new C2 connections or data exfiltration attempts.

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
- DC0082: https://attack.mitre.org/datacomponents/DC0082
- Reviewed: 2026-10-27
