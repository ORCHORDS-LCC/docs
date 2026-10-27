# Clear Network Connection History and Configurations Technique Platform Profile

## Reference

- Technique: **T1070.007 — Clear Network Connection History and Configurations**
- Platforms named in the source: Linux, macOS, Windows, Network Devices

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as Remote Services or External Remote Services. Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries. Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under : * <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default</code> * <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers</code> Windows may also store information about recent RDP connections in files such as <code>C:\Users\\%username%\Documents\Default.rdp</code> and `(a user home directory)AppData\Local\Microsoft\Terminal Server Client\Cache\`. Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`). Malicious network connections may also require changes to third-party applications or network configuration settings, such as Disable or Modify System Firewall or tampering to enable Proxy. Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

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
- T1070.007: https://attack.mitre.org/techniques/T1070/007
- Reviewed: 2026-10-27
