# Disable Windows Event Logging Technique Platform Profile

## Reference

- Technique: **T1562.002 — Disable Windows Event Logging**
- Platforms named in the source: Windows

Adversaries may disable Windows event logging to limit data that can be leveraged for detections and audits. Windows event logs record user and system activity such as login attempts, process creation, and much more. This data is used by security tools and analysts to generate detections. The EventLog service maintains event logs from various system components and applications. By default, the service automatically starts when a system powers on. An audit policy, maintained by the Local Security Policy (secpol.msc), defines which system events the EventLog service logs. Security audit policy settings can be changed by running secpol.msc, then navigating to <code>Security Settings\Local Policies\Audit Policy</code> for basic audit policy settings or <code>Security Settings\Advanced Audit Policy Configuration</code> for advanced audit policy settings. <code>auditpol.exe</code> may also be used to set audit policies. Adversaries may target system-wide logging or just that of a particular application. For example, the Windows EventLog service may be disabled using the <code>Set-Service -Name EventLog -Status Stopped</code> or <code>sc config eventlog start=disabled</code> commands (followed by manually stopping the service using <code>Stop-Service -Name EventLog</code>). Additionally, the service may be disabled by modifying the “Start” value in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog</code> then restarting the system for the change to take effect. There are several ways to disable the EventLog service via registry key modification. First, without Administrator privileges, adversaries may modify the "Start" value in the key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Security</code>, then reboot the system to disable the Security EventLog. Second, with Administrator privilege, adversaries may modify the same values in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-System</code> and <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Application</code> to disable the entire EventLog. Additionally, adversaries may use <code>auditpol</code> and its sub-commands in a command prompt to disable auditing or clear the audit policy. To enable or disable a specified setting or audit category, adversaries may use the <code>/success</code> or <code>/failure</code> parameters. For example, <code>auditpol /set /category:”Account Logon” /success:disable /failure:disable</code> turns off auditing for the Account Logon category. To clear the audit policy, adversaries may run the following lines: <code>auditpol /clear /y</code> or <code>auditpol /remove /allusers</code>. By disabling Windows event logging, adversaries can operate while leaving less evidence of a compromise behind.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1562.002: https://attack.mitre.org/techniques/T1562/002
- Reviewed: 2026-10-27
