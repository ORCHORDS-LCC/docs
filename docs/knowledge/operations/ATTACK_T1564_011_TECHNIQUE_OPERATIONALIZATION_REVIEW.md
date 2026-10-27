# Ignore Process Interrupts Technique Operationalization Review

## Reference

- Technique: **T1564.011 — Ignore Process Interrupts**

Adversaries may evade defensive mechanisms by executing commands that hide from process interrupt signals. Many operating systems use signals to deliver messages to control process behavior. Command interpreters often include specific commands/flags that ignore errors and other hangups, such as when the user of the active session logs off. These interrupt signals may also be used by defensive tools and/or analysts to pause or terminate specified running processes. Adversaries may invoke processes using `nohup`, PowerShell `-ErrorAction SilentlyContinue`, or similar commands that may be immune to hangups. This may enable malicious commands and malware to continue execution through system events that would otherwise terminate its execution, such as users logging off or the termination of its C2 network connection. Hiding from process interrupt signals may allow malware to continue execution, but unlike Trap this does not establish Persistence since the process will not be re-invoked once actually terminated.

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
- T1564.011: https://attack.mitre.org/techniques/T1564/011
- Reviewed: 2026-10-27
