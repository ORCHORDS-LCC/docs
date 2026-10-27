# Firewall Rule Modification Technique Engineering Review

## Reference

- Technique: **DC0051 — Firewall Rule Modification**

The creation, deletion, or alteration of firewall rules to allow or block specific network traffic. Monitoring changes to these rules is critical for detecting misconfigurations, unauthorized access, or malicious attempts to bypass network protections. Examples: - Rule Creation: Adding a new rule to allow inbound traffic on port 3389 (RDP). - Rule Deletion: Deleting a rule that blocks inbound traffic from untrusted IP ranges. - Rule Modification: Changing a rule to allow traffic from "any" source IP instead of a specific trusted range. - Audit Log Metadata: Logs indicating "Firewall rule modified by admin@domain.com." - Platform-Specific Scenarios - Azure: Altering rules in an Azure Network Security Group (NSG). - AWS: Modifying Security Group rules to allow traffic. - Windows: Changes tracked in Security Event Logs (EID 4950 or 4951). This data component can be collected through the following measures: Cloud Control Plane - Azure: Collect rule modification logs from Azure Firewall Activity Logs. - Example Command: `az network firewall policy rule-collection-group rule-collection list --policy-name <policy-name>` - AWS: Use CloudTrail to track `AuthorizeSecurityGroupIngress` or `RevokeSecurityGroupIngress` actions. Example: `aws ec2 describe-security-groups` - Google Cloud: Use gcloud commands to extract firewall rules: `gcloud compute firewall-rules list --format=json` Host-Based Firewalls - Windows: - Collect events from the Windows Security Event Log (EID 4950: A rule has been modified). - Use PowerShell to track rule changes: `Get-NetFirewallRule -PolicyStore PersistentStore` - Linux: - Monitor iptables or nftables rule modifications: `iptables -L -v` - Use auditd for real-time monitoring: `auditctl -w /etc/iptables.rules -p wa` - macOS: Use pfctl to monitor rule changes: `sudo pfctl -sr` SIEM Integration - Collect logs from cloud platforms, host systems, and network appliances for centralized monitoring. API Monitoring - Monitor API calls for firewall rule modifications.

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
- DC0051: https://attack.mitre.org/datacomponents/DC0051
- Reviewed: 2026-10-27
