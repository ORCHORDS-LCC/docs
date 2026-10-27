# At Technique Operationalization Review

## Reference

- Technique: **T1053.002 — At**

Adversaries may abuse the at utility to perform task scheduling for initial or recurring execution of malicious code. The at utility exists as an executable within Windows, Linux, and macOS for scheduling tasks at a specified time and date. Although deprecated in favor of Scheduled Task's schtasks in Windows environments, using at requires that the Task Scheduler service be running, and the user to be logged on as a member of the local Administrators group. In addition to explicitly running the `at` command, adversaries may also schedule a task with at by directly leveraging the Windows Management Instrumentation `Win32_ScheduledJob` WMI class. On Linux and macOS, at may be invoked by the superuser as well as any users added to the <code>at.allow</code> file. If the <code>at.allow</code> file does not exist, the <code>at.deny</code> file is checked. Every username not listed in <code>at.deny</code> is allowed to invoke at. If the <code>at.deny</code> exists and is empty, global use of at is permitted. If neither file exists (which is often the baseline) only the superuser is allowed to use at. Adversaries may use at to execute programs at system startup or on a scheduled basis for Persistence. at can also be abused to conduct remote Execution as part of Lateral Movement and/or to run a process under the context of a specified account (such as SYSTEM). In Linux environments, adversaries may also abuse at to break out of restricted environments by using a task to spawn an interactive system shell or to run system commands. Similarly, at may also be used for Privilege Escalation if the binary is allowed to run as superuser via <code>sudo</code>.

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
- T1053.002: https://attack.mitre.org/techniques/T1053/002
- Reviewed: 2026-10-27
