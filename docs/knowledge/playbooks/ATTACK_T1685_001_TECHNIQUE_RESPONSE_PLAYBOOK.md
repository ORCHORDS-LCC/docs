# Disable or Modify Windows Event Log Technique Response Playbook

## Target technique

**T1685.001 — Disable or Modify Windows Event Log**

- Tactics: defense-impairment
- Platforms: Windows

Adversaries may disable or modify the Windows Event Log to limit data that can be leveraged for detections and audits. Windows Event Log records user and system activity such as login attempts and process creation. This data is used by security tools and analysts to generate detections. The EventLog service maintains event logs from various system components and applications. By default, the service automatically starts when a system powers on. An audit policy, maintained by the Local Security Policy (secpol.msc), defines which system events the EventLog service logs. Security audit policy settings can be changed by running secpol.msc, then navigating to `Security Settings\Local Policies\Audit Policy` for basic audit policy settings or `Security Settings\Advanced Audit Policy Configuration` for advanced audit policy settings. `auditpol.exe` may also be used to set audit policies. Adversaries may target system-wide logging or just that of a particular application. For example, the Windows EventLog service may be disabled using the `Set-Service -Name EventLog -Status Stopped` or `sc config eventlog start=disabled` commands (followed by manually stopping the service using `Stop-Service -Name EventLog`). Additionally, the service may be disabled by modifying the "Start" value in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog` then restarting the system for the change to take effect. There are several ways to disable the EventLog service via registry key modification. Without Administrator privileges, adversaries may modify the "Start" value in the key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Security`, then reboot the system to disable the Security EventLog. With Administrator privilege, adversaries may modify the same values in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-System` and `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Application` to disable the entire EventLog. Additionally, adversaries may use `auditpol` and its sub-commands in a command prompt to disable auditing or clear the audit policy. To enable or disable a specified setting or audit category, adversaries may use the `/success` or `/failure` parameters. For example, `auditpol /set /category:"Account Logon" /success:disable /failure:disable` turns off auditing for the Account Logon category. To clear the audit policy, adversaries may run the following lines: `auditpol /clear /y` or `auditpol /remove /allusers`.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1685.001: https://attack.mitre.org/techniques/T1685/001
- Reviewed: 2026-10-27
