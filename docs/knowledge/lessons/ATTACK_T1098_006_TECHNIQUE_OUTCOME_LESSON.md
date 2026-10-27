# T1098.006 Additional Container Cluster Roles Outcome Lesson

## Authoritative description

- Technique: **T1098.006 — Additional Container Cluster Roles**
- Tactics: persistence, privilege-escalation
- Platforms: Containers

An adversary may add additional roles or permissions to an adversary-controlled user or service account to maintain persistent access to a container orchestration system. For example, an adversary with sufficient permissions may create a RoleBinding or a ClusterRoleBinding to bind a Role or ClusterRole to a Kubernetes account. Where attribute-based access control (ABAC) is in use, an adversary with sufficient permissions may modify a Kubernetes ABAC policy to give the target account additional permissions. This account modification may immediately follow Create Account or other malicious account activity. Adversaries may also modify existing Valid Accounts that they have compromised. Note that where container orchestration systems are deployed in cloud environments, as with Google Kubernetes Engine, Amazon Elastic Kubernetes Service, and Azure Kubernetes Service, cloud-based role-based access control (RBAC) assignments or ABAC policies can often be used in place of or in addition to local permission assignments. In these cases, this technique may be used in conjunction with Additional Cloud Roles.

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
- T1098.006: https://attack.mitre.org/techniques/T1098/006
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
