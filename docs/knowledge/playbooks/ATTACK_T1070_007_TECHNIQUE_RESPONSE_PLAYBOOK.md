# Clear Network Connection History and Configurations Technique Response Playbook

## Target technique

**T1070.007 — Clear Network Connection History and Configurations**

- Tactics: stealth
- Platforms: Linux, macOS, Windows, Network Devices

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as Remote Services or External Remote Services. Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries. Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under : * <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default</code> * <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers</code> Windows may also store information about recent RDP connections in files such as <code>C:\Users\\%username%\Documents\Default.rdp</code> and `(a user home directory)AppData\Local\Microsoft\Terminal Server Client\Cache\`. Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`). Malicious network connections may also require changes to third-party applications or network configuration settings, such as Disable or Modify System Firewall or tampering to enable Proxy. Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

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
- T1070.007: https://attack.mitre.org/techniques/T1070/007
- Reviewed: 2026-10-27
