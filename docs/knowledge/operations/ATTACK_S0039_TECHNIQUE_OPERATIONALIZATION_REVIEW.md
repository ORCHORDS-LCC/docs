# Net Technique Operationalization Review

## Reference

- Technique: **S0039 — Net**

The Net utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. Net has a great deal of functionality, much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through SMB/Windows Admin Shares using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>.

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
- S0039: https://attack.mitre.org/software/S0039
- Reviewed: 2026-10-27
