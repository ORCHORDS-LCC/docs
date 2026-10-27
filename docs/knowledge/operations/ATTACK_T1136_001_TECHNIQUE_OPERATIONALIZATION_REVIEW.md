# Local Account Technique Operationalization Review

## Reference

- Technique: **T1136.001 — Local Account**

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. For example, with a sufficient level of access, the Windows <code>net user /add</code> command can be used to create a local account. In Linux, the `useradd` command can be used, while on macOS systems, the <code>dscl -create</code> command can be used. Local accounts may also be added to network devices, often via common Network Device CLI commands such as <code>username</code>, to ESXi servers via `esxcli system account add`, or to Kubernetes clusters using the `kubectl` utility. Adversaries may also create new local accounts on network firewall management consoles – for example, by exploiting a vulnerable firewall management system, threat actors may be able to establish super-admin accounts that could be used to modify firewall rules and gain further access to the network. Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

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
- T1136.001: https://attack.mitre.org/techniques/T1136/001
- Reviewed: 2026-10-27
