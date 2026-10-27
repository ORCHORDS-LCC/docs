# Cloud Account Technique Engineering Review

## Reference

- Technique: **T1136.003 — Cloud Account**

Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system. In addition to user accounts, cloud accounts may be associated with services. Cloud providers handle the concept of service accounts in different ways. In Azure, service accounts include service principals and managed identities, which can be linked to various resources such as OAuth applications, serverless functions, and virtual machines in order to grant those resources permissions to perform various activities in the environment. In GCP, service accounts can also be linked to specific resources, as well as be impersonated by other accounts for Temporary Elevated Cloud Access. While AWS has no specific concept of service accounts, resources can be directly granted permission to assume roles. Adversaries may create accounts that only have access to specific cloud services, which can reduce the chance of detection. Once an adversary has created a cloud account, they can then manipulate that account to ensure persistence and allow access to additional resources - for example, by adding Additional Cloud Credentials or assigning Additional Cloud Roles.

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
- T1136.003: https://attack.mitre.org/techniques/T1136/003
- Reviewed: 2026-10-27
