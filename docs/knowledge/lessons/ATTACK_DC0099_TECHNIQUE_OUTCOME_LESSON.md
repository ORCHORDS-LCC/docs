# DC0099 Group Enumeration Outcome Lesson

## Authoritative description

- Technique: **DC0099 — Group Enumeration**

Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may exploit high-privilege groups or misconfigurations. Examples: - AWS CLI: `aws iam list-groups` - PowerShell: `Get-ADGroup -Filter *` - (Saas) Google Workspace: Admin SDK Directory API - Azure: `Get-AzureADGroup` - Microsoft 365: Graph API `GET https://graph.microsoft.com/v1.0/groups` *Data Collection Measures:* - Cloud Logging: Enable AWS CloudTrail, Azure Activity Logs, and Google Workspace Admin Logs for group-related actions. - Directory Monitoring: Track logs like AD Event ID 4662 (object operations). - API Monitoring: Log API activity like AWS IAM queries. - SaaS Monitoring: Use platform logs (e.g., Office 365 Unified Audit Logs). - SIEM Integration: Centralize group query tracking.

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
- DC0099: https://attack.mitre.org/datacomponents/DC0099
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
