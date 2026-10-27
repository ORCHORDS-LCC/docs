# Default Accounts Technique Operationalization Review

## Reference

- Technique: **T1078.001 — Default Accounts**

Adversaries may obtain and abuse credentials of a default account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Default accounts are those that are built-into an OS, such as the Guest or Administrator accounts on Windows systems. Default accounts also include default factory/provider set accounts on other types of systems, software, or devices, including the root user account in AWS, the root user account in ESXi, and the default service account in Kubernetes. Default accounts are not limited to client machines; rather, they also include accounts that are preset for equipment such as network devices and computer applications, whether they are internal, open source, or commercial. Appliances that come preset with a username and password combination pose a serious threat to organizations that do not change it post installation, as they are easy targets for an adversary. Similarly, adversaries may also utilize publicly disclosed or stolen Private Keys or credential materials to legitimately connect to remote environments via Remote Services. Default accounts may be created on a system after initial setup by connecting or integrating it with another application. For example, when an ESXi server is connected to a vCenter server, a default privileged account called `vpxuser` is created on the ESXi server. If a threat actor is able to compromise this account’s credentials (for example, via Exploitation for Credential Access on the vCenter host), they will then have access to the ESXi server.

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
- T1078.001: https://attack.mitre.org/techniques/T1078/001
- Reviewed: 2026-10-27
