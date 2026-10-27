# At (Linux) Technique Operationalization Review

## Reference

- Technique: **T1053.001 — At (Linux)**

Adversaries may abuse the at utility to perform task scheduling for initial, recurring, or future execution of malicious code. The at command within Linux operating systems enables administrators to schedule tasks. An adversary may use at in Linux environments to execute programs at system startup or on a scheduled basis for persistence. at can also be abused to conduct remote Execution as part of Lateral Movement and or to run a process under the context of a specified account. Adversaries may also abuse at to break out of restricted environments by using a task to spawn an interactive system shell or to run system commands. Similarly, at may also be used for Privilege Escalation if the binary is allowed to run as superuser via sudo.

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
- T1053.001: https://attack.mitre.org/techniques/T1053/001
- Reviewed: 2026-10-27
