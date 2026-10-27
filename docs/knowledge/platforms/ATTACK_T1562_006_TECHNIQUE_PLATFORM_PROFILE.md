# Indicator Blocking Technique Platform Profile

## Reference

- Technique: **T1562.006 — Indicator Blocking**
- Platforms named in the source: Windows, macOS, Linux, ESXi

An adversary may attempt to block indicators or events typically captured by sensors from being gathered and analyzed. This could include maliciously redirecting or even disabling host-based sensors, such as Event Tracing for Windows (ETW), by tampering settings that control the collection and flow of event telemetry. These settings may be stored on the system in configuration files and/or in the Registry as well as being accessible via administrative utilities such as PowerShell or Windows Management Instrumentation. For example, adversaries may modify the `File` value in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Security</code> to hide their malicious actions in a new or different .evtx log file. This action does not require a system reboot and takes effect immediately. ETW interruption can be achieved multiple ways, however most directly by defining conditions using the PowerShell <code>Set-EtwTraceProvider</code> cmdlet or by interfacing directly with the Registry to make alterations. In the case of network-based reporting of indicators, an adversary may block traffic associated with reporting to prevent central analysis. This may be accomplished by many means, such as stopping a local process responsible for forwarding telemetry and/or creating a host-based firewall rule to block traffic to specific hosts responsible for aggregating events, such as security information and event management (SIEM) products. In Linux environments, adversaries may disable or reconfigure log processing tools such as syslog or nxlog to inhibit detection and monitoring capabilities to facilitate follow on behaviors. ESXi also leverages syslog, which can be reconfigured via commands such as `esxcli system syslog config set` and `esxcli system syslog config reload`.

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
- T1562.006: https://attack.mitre.org/techniques/T1562/006
- Reviewed: 2026-10-27
