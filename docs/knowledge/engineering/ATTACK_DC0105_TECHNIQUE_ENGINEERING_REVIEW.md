# Group Metadata Technique Engineering Review

## Reference

- Technique: **DC0105 — Group Metadata**

Group metadata includes attributes like name, permissions, purpose, and associated user accounts or roles, which adversaries may exploit for privilege escalation. Examples: - Active Directory: `Get-ADGroup -Identity "Domain Admins" -Properties Members, Description` - Azure AD: `Get-AzureADGroup -ObjectId <GroupId>` - Google Workspace: `GET https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>` - AWS IAM: `aws iam list-group-policies --group-name <group_name>` - Office 365: `GET https://graph.microsoft.com/v1.0/groups/<id>` *Data Collection Measures:* - Cloud Logging: - AWS CloudTrail for IAM group-related activities. - Azure AD Sign-In/Audit logs for metadata changes. - Google Admin Activity logs for API calls. - Directory Logging: Log metadata access (e.g., Windows Event ID 4662). - API Monitoring: Log API calls to modify group metadata (e.g., Microsoft Graph API). - SIEM Integration: Centralize group metadata logs for analysis.

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
- DC0105: https://attack.mitre.org/datacomponents/DC0105
- Reviewed: 2026-10-27
