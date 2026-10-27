# T1136.003 Cloud Account Outcome Lesson

## Authoritative description

- Technique: **T1136.003 — Cloud Account**
- Tactics: persistence
- Platforms: IaaS, SaaS, Office Suite, Identity Provider

Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system. In addition to user accounts, cloud accounts may be associated with services. Cloud providers handle the concept of service accounts in different ways. In Azure, service accounts include service principals and managed identities, which can be linked to various resources such as OAuth applications, serverless functions, and virtual machines in order to grant those resources permissions to perform various activities in the environment. In GCP, service accounts can also be linked to specific resources, as well as be impersonated by other accounts for Temporary Elevated Cloud Access. While AWS has no specific concept of service accounts, resources can be directly granted permission to assume roles. Adversaries may create accounts that only have access to specific cloud services, which can reduce the chance of detection. Once an adversary has created a cloud account, they can then manipulate that account to ensure persistence and allow access to additional resources - for example, by adding Additional Cloud Credentials or assigning Additional Cloud Roles.

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
- T1136.003: https://attack.mitre.org/techniques/T1136/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
