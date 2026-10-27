# Cloud Groups Technique Response Playbook

## Target technique

**T1069.003 — Cloud Groups**

- Tactics: discovery
- Platforms: SaaS, IaaS, Office Suite, Identity Provider

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group. With authenticated access there are several tools that can be used to find permissions groups. The <code>Get-MsolRole</code> PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts . Azure CLI (AZ CLI) and the Google Cloud Identity Provider API also provide interfaces to obtain permissions groups. The command <code>az ad user get-member-groups</code> will list groups associated to a user account for Azure while the API endpoint <code>GET https://cloudidentity.googleapis.com/v1/groups</code> lists group resources available to a user for Google. In AWS, the commands `ListRolePolicies` and `ListAttachedRolePolicies` allow users to enumerate the policies attached to a role. Adversaries may attempt to list ACLs for objects to determine the owner and other accounts with access to the object, for example, via the AWS <code>GetBucketAcl</code> API . Using this information an adversary can target accounts with permissions to a given object or leverage accounts they have already compromised to access the object.

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
- T1069.003: https://attack.mitre.org/techniques/T1069/003
- Reviewed: 2026-10-27
