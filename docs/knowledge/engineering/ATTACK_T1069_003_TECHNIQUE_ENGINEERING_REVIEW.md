# Cloud Groups Technique Engineering Review

## Reference

- Technique: **T1069.003 — Cloud Groups**

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group. With authenticated access there are several tools that can be used to find permissions groups. The Get-MsolRole PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts . Azure CLI (AZ CLI) and the Google Cloud Identity Provider API also provide interfaces to obtain permissions groups. The command az ad user get-member-groups will list groups associated to a user account for Azure while the API endpoint GET https://cloudidentity.googleapis.com/v1/groups lists group resources available to a user for Google. In AWS, the commands `ListRolePolicies` and `ListAttachedRolePolicies` allow users to enumerate the policies attached to a role. Adversaries may attempt to list ACLs for objects to determine the owner and other accounts with access to the object, for example, via the AWS GetBucketAcl API . Using this information an adversary can target accounts with permissions to a given object or leverage accounts they have already compromised to access the object.

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
- T1069.003: https://attack.mitre.org/techniques/T1069/003
- Reviewed: 2026-10-27
