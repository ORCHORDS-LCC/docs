# T1087.004 Cloud Account Outcome Lesson

## Authoritative description

- Technique: **T1087.004 — Cloud Account**
- Tactics: discovery
- Platforms: IaaS, Identity Provider, Office Suite, SaaS

Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application. With authenticated access there are several tools that can be used to find accounts. The Get-MsolRoleMember PowerShell cmdlet can be used to obtain account names given a role or permissions group in Office 365. The Azure CLI (AZ CLI) also provides an interface to obtain user accounts with authenticated access to a domain. The command az ad user list will list all users within a domain. The AWS command aws iam list-users may be used to obtain a list of users in the current account while aws iam list-roles can obtain IAM roles that have a specified path prefix. In GCP, gcloud iam service-accounts list and gcloud projects get-iam-policy may be used to obtain a listing of service accounts and users in a project.

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
- T1087.004: https://attack.mitre.org/techniques/T1087/004
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
