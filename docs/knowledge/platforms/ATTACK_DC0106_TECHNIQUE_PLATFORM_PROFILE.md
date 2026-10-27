# Response Metadata Technique Platform Profile

## Reference

- Technique: **DC0106 — Response Metadata**
- Platforms named in the source: not stated

Contextual information about an Internet-facing resource collected during a scan, including details such as open ports, running services, protocols, and versions. This metadata is typically derived from interpreting scan results and helps build a profile of the targeted system. Examples: - Port and Service Details: - Open ports (e.g., 22, 80, 443). - Identified services running on those ports (e.g., SSH, HTTP, HTTPS). - Service Versions: Detected software version information (e.g., Apache 2.4.41, OpenSSH 8.2). - Operating System Information: OS fingerprinting data (e.g., Linux Kernel 5.4.0). - TLS/SSL Certificate Data: Information about the TLS/SSL certificate, such as the expiration date, issuer, and cipher suites. *Data Collection Measures:* - Scanning Tools: - Nmap: Collects port, service, and version information using commands like nmap -sV <IP>. - Masscan: High-speed scanning tool for discovering open ports and active services. - Zmap: Focused on large-scale Internet scanning, collecting metadata about discovered services. - Shodan API: Retrieves scan metadata for publicly exposed devices and services. - Network Logs: - Use logs from firewalls, intrusion detection systems (IDS), or intrusion prevention systems (IPS) to gather metadata from scan attempts. Example: Zeek or Suricata logs for incoming scan traffic. - OSINT Platforms: Platforms like Censys, GreyNoise, or Shodan provide aggregated metadata about Internet-facing resources. - Cloud Metadata Services: AWS Security Hub, Azure Monitor, or GCP Security Command Center can collect and centralize scan-related metadata for Internet-facing resources in cloud environments.

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
- DC0106: https://attack.mitre.org/datacomponents/DC0106
- Reviewed: 2026-10-27
