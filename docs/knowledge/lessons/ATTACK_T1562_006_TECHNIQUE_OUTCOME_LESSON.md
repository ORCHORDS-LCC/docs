# T1562.006 Indicator Blocking Outcome Lesson

## Authoritative description

- Technique: **T1562.006 — Indicator Blocking**
- Tactics: stealth
- Platforms: Windows, macOS, Linux, ESXi

An adversary may attempt to block indicators or events typically captured by sensors from being gathered and analyzed. This could include maliciously redirecting or even disabling host-based sensors, such as Event Tracing for Windows (ETW), by tampering settings that control the collection and flow of event telemetry. These settings may be stored on the system in configuration files and/or in the Registry as well as being accessible via administrative utilities such as PowerShell or Windows Management Instrumentation. For example, adversaries may modify the `File` value in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Security</code> to hide their malicious actions in a new or different .evtx log file. This action does not require a system reboot and takes effect immediately. ETW interruption can be achieved multiple ways, however most directly by defining conditions using the PowerShell <code>Set-EtwTraceProvider</code> cmdlet or by interfacing directly with the Registry to make alterations. In the case of network-based reporting of indicators, an adversary may block traffic associated with reporting to prevent central analysis. This may be accomplished by many means, such as stopping a local process responsible for forwarding telemetry and/or creating a host-based firewall rule to block traffic to specific hosts responsible for aggregating events, such as security information and event management (SIEM) products. In Linux environments, adversaries may disable or reconfigure log processing tools such as syslog or nxlog to inhibit detection and monitoring capabilities to facilitate follow on behaviors. ESXi also leverages syslog, which can be reconfigured via commands such as `esxcli system syslog config set` and `esxcli system syslog config reload`.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1562.006: https://attack.mitre.org/techniques/T1562/006
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
