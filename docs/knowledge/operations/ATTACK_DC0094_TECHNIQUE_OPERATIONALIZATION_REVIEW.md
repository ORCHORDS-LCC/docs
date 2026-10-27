# Group Modification Technique Operationalization Review

## Reference

- Technique: **DC0094 — Group Modification**

Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup). Examples: - Active Directory: - Event ID 4728: Member added to a global group. - Event ID 4732: Member added to a local group. - Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName "New Name"` - AWS IAM: `aws iam update-group --group-name <GroupName> --new-path "/admin/"` - Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>` - Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>` *Data Collection Measures:* - Directory Logging: - Windows: Log EIDs 4728 (add), 4729 (remove). - Azure AD: Enable "Audit logs." - Google Workspace: Enable Admin Activity logs. - Office 365: Use Unified Audit Logs. - Cloud Monitoring: - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`. - Azure: Track modifications via Audit logs. - API Monitoring: Log Google Admin SDK and Microsoft Graph API calls. - SIEM Integration: Centralize and monitor group modification logs.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0094: https://attack.mitre.org/datacomponents/DC0094
- Reviewed: 2026-10-27
