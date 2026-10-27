# Cloud Account Technique Engineering Review

## Reference

- Technique: **T1087.004 — Cloud Account**

Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application. With authenticated access there are several tools that can be used to find accounts. The Get-MsolRoleMember PowerShell cmdlet can be used to obtain account names given a role or permissions group in Office 365. The Azure CLI (AZ CLI) also provides an interface to obtain user accounts with authenticated access to a domain. The command az ad user list will list all users within a domain. The AWS command aws iam list-users may be used to obtain a list of users in the current account while aws iam list-roles can obtain IAM roles that have a specified path prefix. In GCP, gcloud iam service-accounts list and gcloud projects get-iam-policy may be used to obtain a listing of service accounts and users in a project.

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
- T1087.004: https://attack.mitre.org/techniques/T1087/004
- Reviewed: 2026-10-27
