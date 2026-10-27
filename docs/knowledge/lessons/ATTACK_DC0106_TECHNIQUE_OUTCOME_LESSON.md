# DC0106 Response Metadata Outcome Lesson

## Authoritative description

- Technique: **DC0106 — Response Metadata**

Contextual information about an Internet-facing resource collected during a scan, including details such as open ports, running services, protocols, and versions. This metadata is typically derived from interpreting scan results and helps build a profile of the targeted system. Examples: - Port and Service Details: - Open ports (e.g., 22, 80, 443). - Identified services running on those ports (e.g., SSH, HTTP, HTTPS). - Service Versions: Detected software version information (e.g., Apache 2.4.41, OpenSSH 8.2). - Operating System Information: OS fingerprinting data (e.g., Linux Kernel 5.4.0). - TLS/SSL Certificate Data: Information about the TLS/SSL certificate, such as the expiration date, issuer, and cipher suites. *Data Collection Measures:* - Scanning Tools: - Nmap: Collects port, service, and version information using commands like nmap -sV <IP>. - Masscan: High-speed scanning tool for discovering open ports and active services. - Zmap: Focused on large-scale Internet scanning, collecting metadata about discovered services. - Shodan API: Retrieves scan metadata for publicly exposed devices and services. - Network Logs: - Use logs from firewalls, intrusion detection systems (IDS), or intrusion prevention systems (IPS) to gather metadata from scan attempts. Example: Zeek or Suricata logs for incoming scan traffic. - OSINT Platforms: Platforms like Censys, GreyNoise, or Shodan provide aggregated metadata about Internet-facing resources. - Cloud Metadata Services: AWS Security Hub, Azure Monitor, or GCP Security Command Center can collect and centralize scan-related metadata for Internet-facing resources in cloud environments.

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
- DC0106: https://attack.mitre.org/datacomponents/DC0106
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
