# Group Enumeration Technique Response Playbook

## Target technique

**DC0099 — Group Enumeration**


Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may exploit high-privilege groups or misconfigurations. Examples: - AWS CLI: `aws iam list-groups` - PowerShell: `Get-ADGroup -Filter *` - (Saas) Google Workspace: Admin SDK Directory API - Azure: `Get-AzureADGroup` - Microsoft 365: Graph API `GET https://graph.microsoft.com/v1.0/groups` *Data Collection Measures:* - Cloud Logging: Enable AWS CloudTrail, Azure Activity Logs, and Google Workspace Admin Logs for group-related actions. - Directory Monitoring: Track logs like AD Event ID 4662 (object operations). - API Monitoring: Log API activity like AWS IAM queries. - SaaS Monitoring: Use platform logs (e.g., Office 365 Unified Audit Logs). - SIEM Integration: Centralize group query tracking.

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
- DC0099: https://attack.mitre.org/datacomponents/DC0099
- Reviewed: 2026-10-27
