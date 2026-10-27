# DC0094 Group Modification Outcome Lesson

## Authoritative description

- Technique: **DC0094 — Group Modification**

Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup). Examples: - Active Directory: - Event ID 4728: Member added to a global group. - Event ID 4732: Member added to a local group. - Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName "New Name"` - AWS IAM: `aws iam update-group --group-name <GroupName> --new-path "/admin/"` - Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>` - Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>` *Data Collection Measures:* - Directory Logging: - Windows: Log EIDs 4728 (add), 4729 (remove). - Azure AD: Enable "Audit logs." - Google Workspace: Enable Admin Activity logs. - Office 365: Use Unified Audit Logs. - Cloud Monitoring: - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`. - Azure: Track modifications via Audit logs. - API Monitoring: Log Google Admin SDK and Microsoft Graph API calls. - SIEM Integration: Centralize and monitor group modification logs.

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
- DC0094: https://attack.mitre.org/datacomponents/DC0094
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
