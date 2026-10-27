# DC0044 Firewall Enumeration Outcome Lesson

## Authoritative description

- Technique: **DC0044 — Firewall Enumeration**

Querying and extracting a list of available firewalls or their associated configurations and rules. This activity can occur across host systems and cloud control planes, providing insight into the state and configuration of firewalls that protect the environment. Examples: - Querying Host-Based Firewalls: Using Windows PowerShell commands like `Get-NetFirewallRule` or Linux commands such as `iptables -L` or `firewalld --list-all`. - Cloud Firewall Rule Listing: Running commands like `az network firewall list` for Azure or `aws ec2 describe-security-groups` for AWS. - Using Management APIs: Leveraging APIs like Google Cloud Firewall's `list` API method or AWS's DescribeSecurityGroups API. Identifying Misconfigurations: Extracting firewall rules to identify “allow all” policies or rules that lack logging. - Enumerating with CLI Tools: Using CLI commands like `gcloud compute firewall-rules list` to extract firewall settings in Google Cloud.

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
- DC0044: https://attack.mitre.org/datacomponents/DC0044
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
