# Firewall Rule Modification Technique Platform Profile

## Reference

- Technique: **DC0051 — Firewall Rule Modification**
- Platforms named in the source: not stated

The creation, deletion, or alteration of firewall rules to allow or block specific network traffic. Monitoring changes to these rules is critical for detecting misconfigurations, unauthorized access, or malicious attempts to bypass network protections. Examples: - Rule Creation: Adding a new rule to allow inbound traffic on port 3389 (RDP). - Rule Deletion: Deleting a rule that blocks inbound traffic from untrusted IP ranges. - Rule Modification: Changing a rule to allow traffic from "any" source IP instead of a specific trusted range. - Audit Log Metadata: Logs indicating "Firewall rule modified by admin@domain.com." - Platform-Specific Scenarios - Azure: Altering rules in an Azure Network Security Group (NSG). - AWS: Modifying Security Group rules to allow traffic. - Windows: Changes tracked in Security Event Logs (EID 4950 or 4951). This data component can be collected through the following measures: Cloud Control Plane - Azure: Collect rule modification logs from Azure Firewall Activity Logs. - Example Command: `az network firewall policy rule-collection-group rule-collection list --policy-name <policy-name>` - AWS: Use CloudTrail to track `AuthorizeSecurityGroupIngress` or `RevokeSecurityGroupIngress` actions. Example: `aws ec2 describe-security-groups` - Google Cloud: Use gcloud commands to extract firewall rules: `gcloud compute firewall-rules list --format=json` Host-Based Firewalls - Windows: - Collect events from the Windows Security Event Log (EID 4950: A rule has been modified). - Use PowerShell to track rule changes: `Get-NetFirewallRule -PolicyStore PersistentStore` - Linux: - Monitor iptables or nftables rule modifications: `iptables -L -v` - Use auditd for real-time monitoring: `auditctl -w /etc/iptables.rules -p wa` - macOS: Use pfctl to monitor rule changes: `sudo pfctl -sr` SIEM Integration - Collect logs from cloud platforms, host systems, and network appliances for centralized monitoring. API Monitoring - Monitor API calls for firewall rule modifications.

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
- DC0051: https://attack.mitre.org/datacomponents/DC0051
- Reviewed: 2026-10-27
