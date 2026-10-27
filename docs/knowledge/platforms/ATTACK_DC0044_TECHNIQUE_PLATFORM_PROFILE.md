# Firewall Enumeration Technique Platform Profile

## Reference

- Technique: **DC0044 — Firewall Enumeration**
- Platforms named in the source: not stated

Querying and extracting a list of available firewalls or their associated configurations and rules. This activity can occur across host systems and cloud control planes, providing insight into the state and configuration of firewalls that protect the environment. Examples: - Querying Host-Based Firewalls: Using Windows PowerShell commands like `Get-NetFirewallRule` or Linux commands such as `iptables -L` or `firewalld --list-all`. - Cloud Firewall Rule Listing: Running commands like `az network firewall list` for Azure or `aws ec2 describe-security-groups` for AWS. - Using Management APIs: Leveraging APIs like Google Cloud Firewall's `list` API method or AWS's DescribeSecurityGroups API. Identifying Misconfigurations: Extracting firewall rules to identify “allow all” policies or rules that lack logging. - Enumerating with CLI Tools: Using CLI commands like `gcloud compute firewall-rules list` to extract firewall settings in Google Cloud.

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
- DC0044: https://attack.mitre.org/datacomponents/DC0044
- Reviewed: 2026-10-27
