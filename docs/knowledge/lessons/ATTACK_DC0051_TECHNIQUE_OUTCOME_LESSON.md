# DC0051 Firewall Rule Modification Outcome Lesson

## Authoritative description

- Technique: **DC0051 — Firewall Rule Modification**

The creation, deletion, or alteration of firewall rules to allow or block specific network traffic. Monitoring changes to these rules is critical for detecting misconfigurations, unauthorized access, or malicious attempts to bypass network protections. Examples: - Rule Creation: Adding a new rule to allow inbound traffic on port 3389 (RDP). - Rule Deletion: Deleting a rule that blocks inbound traffic from untrusted IP ranges. - Rule Modification: Changing a rule to allow traffic from "any" source IP instead of a specific trusted range. - Audit Log Metadata: Logs indicating "Firewall rule modified by admin@domain.com." - Platform-Specific Scenarios - Azure: Altering rules in an Azure Network Security Group (NSG). - AWS: Modifying Security Group rules to allow traffic. - Windows: Changes tracked in Security Event Logs (EID 4950 or 4951). This data component can be collected through the following measures: Cloud Control Plane - Azure: Collect rule modification logs from Azure Firewall Activity Logs. - Example Command: `az network firewall policy rule-collection-group rule-collection list --policy-name <policy-name>` - AWS: Use CloudTrail to track `AuthorizeSecurityGroupIngress` or `RevokeSecurityGroupIngress` actions. Example: `aws ec2 describe-security-groups` - Google Cloud: Use gcloud commands to extract firewall rules: `gcloud compute firewall-rules list --format=json` Host-Based Firewalls - Windows: - Collect events from the Windows Security Event Log (EID 4950: A rule has been modified). - Use PowerShell to track rule changes: `Get-NetFirewallRule -PolicyStore PersistentStore` - Linux: - Monitor iptables or nftables rule modifications: `iptables -L -v` - Use auditd for real-time monitoring: `auditctl -w /etc/iptables.rules -p wa` - macOS: Use pfctl to monitor rule changes: `sudo pfctl -sr` SIEM Integration - Collect logs from cloud platforms, host systems, and network appliances for centralized monitoring. API Monitoring - Monitor API calls for firewall rule modifications.

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
- DC0051: https://attack.mitre.org/datacomponents/DC0051
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
