# Response Content Technique Platform Profile

## Reference

- Technique: **DC0104 — Response Content**
- Platforms named in the source: not stated

Captured network traffic that provides details about responses received during an internet scan. This data includes both protocol header values (e.g., HTTP status codes, IP headers, or DNS response codes) and response body content (e.g., HTML, JSON, or raw data). Examples: - HTTP Scan: A web server responds to a probe with an HTTP 200 status code and an HTML body indicating the default page is accessible. - DNS Scan: A DNS server replies to a query with a resolved IP address for a domain, along with details like Time-To-Live (TTL) and authoritative information. - TCP Banner Grab: A service listening on a port (e.g., SSH or FTP) responds with a banner containing service name, version, or other metadata.

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
- DC0104: https://attack.mitre.org/datacomponents/DC0104
- Reviewed: 2026-10-27
