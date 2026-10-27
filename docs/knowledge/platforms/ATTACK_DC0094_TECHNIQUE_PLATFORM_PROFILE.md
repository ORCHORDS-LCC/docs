# Group Modification Technique Platform Profile

## Reference

- Technique: **DC0094 — Group Modification**
- Platforms named in the source: not stated

Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup). Examples: - Active Directory: - Event ID 4728: Member added to a global group. - Event ID 4732: Member added to a local group. - Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName "New Name"` - AWS IAM: `aws iam update-group --group-name <GroupName> --new-path "/admin/"` - Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>` - Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>` *Data Collection Measures:* - Directory Logging: - Windows: Log EIDs 4728 (add), 4729 (remove). - Azure AD: Enable "Audit logs." - Google Workspace: Enable Admin Activity logs. - Office 365: Use Unified Audit Logs. - Cloud Monitoring: - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`. - Azure: Track modifications via Audit logs. - API Monitoring: Log Google Admin SDK and Microsoft Graph API calls. - SIEM Integration: Centralize and monitor group modification logs.

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
- DC0094: https://attack.mitre.org/datacomponents/DC0094
- Reviewed: 2026-10-27
