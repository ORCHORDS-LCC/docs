# Active DNS Technique Engineering Review

## Reference

- Technique: **DC0103 — Active DNS**

"Domain Name: Active DNS" data component captures queried DNS registry data that highlights current domain-to-IP address resolutions. This data includes both direct queries to DNS servers and records that provide mappings between domain names and associated IP addresses. It serves as a critical resource for tracking active infrastructure and understanding the network footprint of an organization or adversary. Examples: - DNS Query Example: `nslookup example.com`, `dig example.com A` - PTR Record Example: `dig -x 192.168.1.1` - Tracking Malicious Domains: DNS logs reveal repeated queries to suspicious domains like malicious-site.com. The IPs resolved by these domains may be indicators of compromise (IOCs). - DNS Record Types - A/AAAA Record: Maps domain names to IP addresses (IPv4/IPv6). - CNAME Record: Canonical name records, often used for redirects. - MX Record: Mail exchange records, used to route emails. - TXT Record: Can include security information like SPF or DKIM policies. - SOA Record: Start of authority record for domain management. - NS Record: Lists authoritative name servers for the domain. This data component can be collected through the following measures: - System Utilities: Use built-in tools like `nslookup`, `dig`, or host on Linux, macOS, and Windows to perform active DNS queries. - DNS Logging - Windows DNS Server: Enable DNS Analytical Logging to capture DNS queries and responses. - Bind DNS: Enable query logging in the named.conf file. - Cloud Provider DNS Logging - AWS Route 53: Enable query logging through CloudWatch or S3: - Google Cloud DNS: Enable logging for Cloud DNS queries through Google Cloud Logging. - Network Traffic Monitoring: Use tools like Wireshark or Zeek to analyze DNS queries within network traffic. - Security Information and Event Management (SIEM) Integration: Aggregate DNS logs in a SIEM like Splunk to create alerts and monitor patterns. - Public OSINT Tools: Use OSINT platforms like VirusTotal, or PassiveTotal to collect information on domains and their associated IP addresses.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0103: https://attack.mitre.org/datacomponents/DC0103
- Reviewed: 2026-10-27
