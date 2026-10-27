# Active DNS Technique Response Playbook

## Target technique

**DC0103 — Active DNS**


"Domain Name: Active DNS" data component captures queried DNS registry data that highlights current domain-to-IP address resolutions. This data includes both direct queries to DNS servers and records that provide mappings between domain names and associated IP addresses. It serves as a critical resource for tracking active infrastructure and understanding the network footprint of an organization or adversary. Examples: - DNS Query Example: `nslookup example.com`, `dig example.com A` - PTR Record Example: `dig -x 192.168.1.1` - Tracking Malicious Domains: DNS logs reveal repeated queries to suspicious domains like malicious-site.com. The IPs resolved by these domains may be indicators of compromise (IOCs). - DNS Record Types - A/AAAA Record: Maps domain names to IP addresses (IPv4/IPv6). - CNAME Record: Canonical name records, often used for redirects. - MX Record: Mail exchange records, used to route emails. - TXT Record: Can include security information like SPF or DKIM policies. - SOA Record: Start of authority record for domain management. - NS Record: Lists authoritative name servers for the domain. This data component can be collected through the following measures: - System Utilities: Use built-in tools like `nslookup`, `dig`, or host on Linux, macOS, and Windows to perform active DNS queries. - DNS Logging - Windows DNS Server: Enable DNS Analytical Logging to capture DNS queries and responses. - Bind DNS: Enable query logging in the named.conf file. - Cloud Provider DNS Logging - AWS Route 53: Enable query logging through CloudWatch or S3: - Google Cloud DNS: Enable logging for Cloud DNS queries through Google Cloud Logging. - Network Traffic Monitoring: Use tools like Wireshark or Zeek to analyze DNS queries within network traffic. - Security Information and Event Management (SIEM) Integration: Aggregate DNS logs in a SIEM like Splunk to create alerts and monitor patterns. - Public OSINT Tools: Use OSINT platforms like VirusTotal, or PassiveTotal to collect information on domains and their associated IP addresses.

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
- DC0103: https://attack.mitre.org/datacomponents/DC0103
- Reviewed: 2026-10-27
