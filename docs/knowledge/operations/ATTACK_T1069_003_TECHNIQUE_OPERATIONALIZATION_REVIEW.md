# Cloud Groups Technique Operationalization Review

## Reference

- Technique: **T1069.003 — Cloud Groups**

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group. With authenticated access there are several tools that can be used to find permissions groups. The <code>Get-MsolRole</code> PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts . Azure CLI (AZ CLI) and the Google Cloud Identity Provider API also provide interfaces to obtain permissions groups. The command <code>az ad user get-member-groups</code> will list groups associated to a user account for Azure while the API endpoint <code>GET https://cloudidentity.googleapis.com/v1/groups</code> lists group resources available to a user for Google. In AWS, the commands `ListRolePolicies` and `ListAttachedRolePolicies` allow users to enumerate the policies attached to a role. Adversaries may attempt to list ACLs for objects to determine the owner and other accounts with access to the object, for example, via the AWS <code>GetBucketAcl</code> API . Using this information an adversary can target accounts with permissions to a given object or leverage accounts they have already compromised to access the object.

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
- T1069.003: https://attack.mitre.org/techniques/T1069/003
- Reviewed: 2026-10-27
