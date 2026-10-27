# DC0105 Group Metadata Outcome Lesson

## Authoritative description

- Technique: **DC0105 — Group Metadata**

Group metadata includes attributes like name, permissions, purpose, and associated user accounts or roles, which adversaries may exploit for privilege escalation. Examples: - Active Directory: `Get-ADGroup -Identity "Domain Admins" -Properties Members, Description` - Azure AD: `Get-AzureADGroup -ObjectId <GroupId>` - Google Workspace: `GET https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>` - AWS IAM: `aws iam list-group-policies --group-name <group_name>` - Office 365: `GET https://graph.microsoft.com/v1.0/groups/<id>` *Data Collection Measures:* - Cloud Logging: - AWS CloudTrail for IAM group-related activities. - Azure AD Sign-In/Audit logs for metadata changes. - Google Admin Activity logs for API calls. - Directory Logging: Log metadata access (e.g., Windows Event ID 4662). - API Monitoring: Log API calls to modify group metadata (e.g., Microsoft Graph API). - SIEM Integration: Centralize group metadata logs for analysis.

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
- DC0105: https://attack.mitre.org/datacomponents/DC0105
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
