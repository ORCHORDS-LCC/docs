# Firewall Metadata Technique Response Playbook

## Target technique

**DC0053 — Firewall Metadata**


Contextual information about firewalls, including their configurations, policies, status, and other details such as names and associated rules. This metadata provides valuable insights into the operational state and configurations of firewalls, both in cloud control planes and host systems. Examples: - Firewall Name and Configuration: The name, type, and purpose of a firewall such as "Azure Firewall - Production Environment." - Policy Details: Capturing firewall policy details, such as "Allow inbound TCP 443 to web servers." - Firewall Status: Status indicators like "Active," "Disabled," or "Pending Updates." - Audit Log Metadata: Log entries showing administrative changes, such as "Policy modified by admin@domain.com." - Rules Associated with Firewalls: Rules specifying source/destination IP ranges, protocols, and ports. - Tagging Information: Tags like "Environment: Production" or "Owner: NetworkOps." This data component can be collected through the following measures: Cloud Control Plane - Azure: Use Azure Activity Logs and Network Watcher to collect metadata for Azure Firewall. - Example: `az network firewall show --name <firewall-name>` - AWS: Use AWS CloudTrail and describe commands: `aws ec2 describe-security-groups` - Google Cloud: Use gcloud commands to extract metadata: `gcloud compute firewall-rules list --format=json` Host-Based Firewalls - Windows: Use PowerShell to gather metadata: `Get-NetFirewallRule -PolicyStore PersistentStore` - Linux: Query iptables or nftables rulesets: `iptables -S` - macOS: Use pfctl to extract metadata: `sudo pfctl -sr` SIEM Integration - Collect logs from cloud platforms, host systems, and network appliances. API Monitoring - Monitor API calls for metadata requests. Example (AWS): `Capture DescribeSecurityGroups or DescribeNetworkAcls` calls via CloudTrail. Endpoint Detection and Response (EDR) - Use EDR solutions to monitor firewall management tools for configuration changes or queries.

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
- DC0053: https://attack.mitre.org/datacomponents/DC0053
- Reviewed: 2026-10-27
