# Active DNS Technique Platform Profile

## Reference

- Technique: **DC0103 — Active DNS**
- Platforms named in the source: not stated

"Domain Name: Active DNS" data component captures queried DNS registry data that highlights current domain-to-IP address resolutions. This data includes both direct queries to DNS servers and records that provide mappings between domain names and associated IP addresses. It serves as a critical resource for tracking active infrastructure and understanding the network footprint of an organization or adversary. Examples: - DNS Query Example: `nslookup example.com`, `dig example.com A` - PTR Record Example: `dig -x 192.168.1.1` - Tracking Malicious Domains: DNS logs reveal repeated queries to suspicious domains like malicious-site.com. The IPs resolved by these domains may be indicators of compromise (IOCs). - DNS Record Types - A/AAAA Record: Maps domain names to IP addresses (IPv4/IPv6). - CNAME Record: Canonical name records, often used for redirects. - MX Record: Mail exchange records, used to route emails. - TXT Record: Can include security information like SPF or DKIM policies. - SOA Record: Start of authority record for domain management. - NS Record: Lists authoritative name servers for the domain. This data component can be collected through the following measures: - System Utilities: Use built-in tools like `nslookup`, `dig`, or host on Linux, macOS, and Windows to perform active DNS queries. - DNS Logging - Windows DNS Server: Enable DNS Analytical Logging to capture DNS queries and responses. - Bind DNS: Enable query logging in the named.conf file. - Cloud Provider DNS Logging - AWS Route 53: Enable query logging through CloudWatch or S3: - Google Cloud DNS: Enable logging for Cloud DNS queries through Google Cloud Logging. - Network Traffic Monitoring: Use tools like Wireshark or Zeek to analyze DNS queries within network traffic. - Security Information and Event Management (SIEM) Integration: Aggregate DNS logs in a SIEM like Splunk to create alerts and monitor patterns. - Public OSINT Tools: Use OSINT platforms like VirusTotal, or PassiveTotal to collect information on domains and their associated IP addresses.

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
- DC0103: https://attack.mitre.org/datacomponents/DC0103
- Reviewed: 2026-10-27
