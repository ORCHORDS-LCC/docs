# Group Modification Technique Engineering Review

## Reference

- Technique: **DC0094 — Group Modification**

Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup). Examples: - Active Directory: - Event ID 4728: Member added to a global group. - Event ID 4732: Member added to a local group. - Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName "New Name"` - AWS IAM: `aws iam update-group --group-name <GroupName> --new-path "/admin/"` - Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>` - Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>` *Data Collection Measures:* - Directory Logging: - Windows: Log EIDs 4728 (add), 4729 (remove). - Azure AD: Enable "Audit logs." - Google Workspace: Enable Admin Activity logs. - Office 365: Use Unified Audit Logs. - Cloud Monitoring: - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`. - Azure: Track modifications via Audit logs. - API Monitoring: Log Google Admin SDK and Microsoft Graph API calls. - SIEM Integration: Centralize and monitor group modification logs.

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
- DC0094: https://attack.mitre.org/datacomponents/DC0094
- Reviewed: 2026-10-27
