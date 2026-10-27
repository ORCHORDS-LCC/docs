# Cloud Account Technique Operationalization Review

## Reference

- Technique: **T1087.004 — Cloud Account**

Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application. With authenticated access there are several tools that can be used to find accounts. The <code>Get-MsolRoleMember</code> PowerShell cmdlet can be used to obtain account names given a role or permissions group in Office 365. The Azure CLI (AZ CLI) also provides an interface to obtain user accounts with authenticated access to a domain. The command <code>az ad user list</code> will list all users within a domain. The AWS command <code>aws iam list-users</code> may be used to obtain a list of users in the current account while <code>aws iam list-roles</code> can obtain IAM roles that have a specified path prefix. In GCP, <code>gcloud iam service-accounts list</code> and <code>gcloud projects get-iam-policy</code> may be used to obtain a listing of service accounts and users in a project.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1087.004: https://attack.mitre.org/techniques/T1087/004
- Reviewed: 2026-10-27
