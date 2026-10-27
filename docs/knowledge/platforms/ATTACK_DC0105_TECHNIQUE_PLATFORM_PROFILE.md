# Group Metadata Technique Platform Profile

## Reference

- Technique: **DC0105 — Group Metadata**
- Platforms named in the source: not stated

Group metadata includes attributes like name, permissions, purpose, and associated user accounts or roles, which adversaries may exploit for privilege escalation. Examples: - Active Directory: `Get-ADGroup -Identity "Domain Admins" -Properties Members, Description` - Azure AD: `Get-AzureADGroup -ObjectId <GroupId>` - Google Workspace: `GET https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>` - AWS IAM: `aws iam list-group-policies --group-name <group_name>` - Office 365: `GET https://graph.microsoft.com/v1.0/groups/<id>` *Data Collection Measures:* - Cloud Logging: - AWS CloudTrail for IAM group-related activities. - Azure AD Sign-In/Audit logs for metadata changes. - Google Admin Activity logs for API calls. - Directory Logging: Log metadata access (e.g., Windows Event ID 4662). - API Monitoring: Log API calls to modify group metadata (e.g., Microsoft Graph API). - SIEM Integration: Centralize group metadata logs for analysis.

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
- DC0105: https://attack.mitre.org/datacomponents/DC0105
- Reviewed: 2026-10-27
