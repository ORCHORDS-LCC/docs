# Cloud Account Technique Response Playbook

## Target technique

**T1087.004 — Cloud Account**

- Tactics: discovery
- Platforms: IaaS, Identity Provider, Office Suite, SaaS

Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application. With authenticated access there are several tools that can be used to find accounts. The Get-MsolRoleMember PowerShell cmdlet can be used to obtain account names given a role or permissions group in Office 365. The Azure CLI (AZ CLI) also provides an interface to obtain user accounts with authenticated access to a domain. The command az ad user list will list all users within a domain. The AWS command aws iam list-users may be used to obtain a list of users in the current account while aws iam list-roles can obtain IAM roles that have a specified path prefix. In GCP, gcloud iam service-accounts list and gcloud projects get-iam-policy may be used to obtain a listing of service accounts and users in a project.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1087.004: https://attack.mitre.org/techniques/T1087/004
- Reviewed: 2026-10-27
