# Group Enumeration Technique Engineering Review

## Reference

- Technique: **DC0099 — Group Enumeration**

Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may exploit high-privilege groups or misconfigurations. Examples: - AWS CLI: `aws iam list-groups` - PowerShell: `Get-ADGroup -Filter *` - (Saas) Google Workspace: Admin SDK Directory API - Azure: `Get-AzureADGroup` - Microsoft 365: Graph API `GET https://graph.microsoft.com/v1.0/groups` *Data Collection Measures:* - Cloud Logging: Enable AWS CloudTrail, Azure Activity Logs, and Google Workspace Admin Logs for group-related actions. - Directory Monitoring: Track logs like AD Event ID 4662 (object operations). - API Monitoring: Log API activity like AWS IAM queries. - SaaS Monitoring: Use platform logs (e.g., Office 365 Unified Audit Logs). - SIEM Integration: Centralize group query tracking.

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
- DC0099: https://attack.mitre.org/datacomponents/DC0099
- Reviewed: 2026-10-27
