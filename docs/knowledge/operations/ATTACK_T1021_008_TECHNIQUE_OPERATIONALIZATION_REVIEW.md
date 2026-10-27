# Direct Cloud VM Connections Technique Operationalization Review

## Reference

- Technique: **T1021.008 — Direct Cloud VM Connections**

Adversaries may leverage Valid Accounts to log directly into accessible cloud hosted compute infrastructure through cloud native methods. Many cloud providers offer interactive connections to virtual infrastructure that can be accessed through the Cloud API, such as Azure Serial Console, AWS EC2 Instance Connect, and AWS System Manager.. Methods of authentication for these connections can include passwords, application access tokens, or SSH keys. These cloud native methods may, by default, allow for privileged access on the host with SYSTEM or root level access. Adversaries may utilize these cloud native methods to directly access virtual infrastructure and pivot through an environment. These connections typically provide direct console access to the VM rather than the execution of scripts (i.e., Cloud Administration Command).

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
- T1021.008: https://attack.mitre.org/techniques/T1021/008
- Reviewed: 2026-10-27
