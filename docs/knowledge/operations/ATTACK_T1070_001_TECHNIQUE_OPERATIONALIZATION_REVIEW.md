# Clear Windows Event Logs Technique Operationalization Review

## Reference

- Technique: **T1070.001 — Clear Windows Event Logs**

Adversaries may clear Windows Event Logs to hide the activity of an intrusion. Windows Event Logs are a record of a computer's alerts and notifications. There are three system-defined sources of events: System, Application, and Security, with five event types: Error, Warning, Information, Success Audit, and Failure Audit. With administrator privileges, the event logs can be cleared with the following utility commands: * <code>wevtutil cl system</code> * <code>wevtutil cl application</code> * <code>wevtutil cl security</code> These logs may also be cleared through other mechanisms, such as the event viewer GUI or PowerShell. For example, adversaries may use the PowerShell command <code>Remove-EventLog -LogName Security</code> to delete the Security EventLog and after reboot, disable future logging. Note: events may still be generated and logged in the .evtx file between the time the command is run and the reboot. Adversaries may also attempt to clear logs by directly deleting the stored log files within `C:\Windows\System32\winevt\logs\`.

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
- T1070.001: https://attack.mitre.org/techniques/T1070/001
- Reviewed: 2026-10-27
