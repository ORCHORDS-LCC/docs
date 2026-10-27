# Firewall Metadata Technique Platform Profile

## Reference

- Technique: **DC0053 — Firewall Metadata**
- Platforms named in the source: not stated

Contextual information about firewalls, including their configurations, policies, status, and other details such as names and associated rules. This metadata provides valuable insights into the operational state and configurations of firewalls, both in cloud control planes and host systems. Examples: - Firewall Name and Configuration: The name, type, and purpose of a firewall such as "Azure Firewall - Production Environment." - Policy Details: Capturing firewall policy details, such as "Allow inbound TCP 443 to web servers." - Firewall Status: Status indicators like "Active," "Disabled," or "Pending Updates." - Audit Log Metadata: Log entries showing administrative changes, such as "Policy modified by admin@domain.com." - Rules Associated with Firewalls: Rules specifying source/destination IP ranges, protocols, and ports. - Tagging Information: Tags like "Environment: Production" or "Owner: NetworkOps." This data component can be collected through the following measures: Cloud Control Plane - Azure: Use Azure Activity Logs and Network Watcher to collect metadata for Azure Firewall. - Example: `az network firewall show --name <firewall-name>` - AWS: Use AWS CloudTrail and describe commands: `aws ec2 describe-security-groups` - Google Cloud: Use gcloud commands to extract metadata: `gcloud compute firewall-rules list --format=json` Host-Based Firewalls - Windows: Use PowerShell to gather metadata: `Get-NetFirewallRule -PolicyStore PersistentStore` - Linux: Query iptables or nftables rulesets: `iptables -S` - macOS: Use pfctl to extract metadata: `sudo pfctl -sr` SIEM Integration - Collect logs from cloud platforms, host systems, and network appliances. API Monitoring - Monitor API calls for metadata requests. Example (AWS): `Capture DescribeSecurityGroups or DescribeNetworkAcls` calls via CloudTrail. Endpoint Detection and Response (EDR) - Use EDR solutions to monitor firewall management tools for configuration changes or queries.

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
- DC0053: https://attack.mitre.org/datacomponents/DC0053
- Reviewed: 2026-10-27
