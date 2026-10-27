# T1070.007 Clear Network Connection History and Configurations Outcome Lesson

## Authoritative description

- Technique: **T1070.007 — Clear Network Connection History and Configurations**
- Tactics: stealth
- Platforms: Linux, macOS, Windows, Network Devices

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as Remote Services or External Remote Services. Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries. Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under : * HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default * HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers Windows may also store information about recent RDP connections in files such as C:\Users\\%username%\Documents\Default.rdp and `(a user home directory)AppData\Local\Microsoft\Terminal Server Client\Cache\`. Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`). Malicious network connections may also require changes to third-party applications or network configuration settings, such as Disable or Modify System Firewall or tampering to enable Proxy. Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

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
- T1070.007: https://attack.mitre.org/techniques/T1070/007
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
