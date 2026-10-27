# Clear Network Connection History and Configurations Technique Engineering Review

## Reference

- Technique: **T1070.007 — Clear Network Connection History and Configurations**

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as Remote Services or External Remote Services. Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries. Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under : * HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default * HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers Windows may also store information about recent RDP connections in files such as C:\Users\\%username%\Documents\Default.rdp and `(a user home directory)AppData\Local\Microsoft\Terminal Server Client\Cache\`. Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`). Malicious network connections may also require changes to third-party applications or network configuration settings, such as Disable or Modify System Firewall or tampering to enable Proxy. Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1070.007: https://attack.mitre.org/techniques/T1070/007
- Reviewed: 2026-10-27
