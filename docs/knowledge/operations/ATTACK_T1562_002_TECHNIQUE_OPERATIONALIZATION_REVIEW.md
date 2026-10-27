# Disable Windows Event Logging Technique Operationalization Review

## Reference

- Technique: **T1562.002 — Disable Windows Event Logging**

Adversaries may disable Windows event logging to limit data that can be leveraged for detections and audits. Windows event logs record user and system activity such as login attempts, process creation, and much more. This data is used by security tools and analysts to generate detections. The EventLog service maintains event logs from various system components and applications. By default, the service automatically starts when a system powers on. An audit policy, maintained by the Local Security Policy (secpol.msc), defines which system events the EventLog service logs. Security audit policy settings can be changed by running secpol.msc, then navigating to Security Settings\Local Policies\Audit Policy for basic audit policy settings or Security Settings\Advanced Audit Policy Configuration for advanced audit policy settings. auditpol.exe may also be used to set audit policies. Adversaries may target system-wide logging or just that of a particular application. For example, the Windows EventLog service may be disabled using the Set-Service -Name EventLog -Status Stopped or sc config eventlog start=disabled commands (followed by manually stopping the service using Stop-Service -Name EventLog). Additionally, the service may be disabled by modifying the “Start” value in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog then restarting the system for the change to take effect. There are several ways to disable the EventLog service via registry key modification. First, without Administrator privileges, adversaries may modify the "Start" value in the key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Security, then reboot the system to disable the Security EventLog. Second, with Administrator privilege, adversaries may modify the same values in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-System and HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Application to disable the entire EventLog. Additionally, adversaries may use auditpol and its sub-commands in a command prompt to disable auditing or clear the audit policy. To enable or disable a specified setting or audit category, adversaries may use the /success or /failure parameters. For example, auditpol /set /category:”Account Logon” /success:disable /failure:disable turns off auditing for the Account Logon category. To clear the audit policy, adversaries may run the following lines: auditpol /clear /y or auditpol /remove /allusers. By disabling Windows event logging, adversaries can operate while leaving less evidence of a compromise behind.

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
- T1562.002: https://attack.mitre.org/techniques/T1562/002
- Reviewed: 2026-10-27
