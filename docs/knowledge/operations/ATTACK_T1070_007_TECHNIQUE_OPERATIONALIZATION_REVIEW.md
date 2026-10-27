# Clear Network Connection History and Configurations Technique Operationalization Review

## Reference

- Technique: **T1070.007 — Clear Network Connection History and Configurations**

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as Remote Services or External Remote Services. Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries. Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under : * HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default * HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers Windows may also store information about recent RDP connections in files such as C:\Users\\%username%\Documents\Default.rdp and `(a user home directory)AppData\Local\Microsoft\Terminal Server Client\Cache\`. Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`). Malicious network connections may also require changes to third-party applications or network configuration settings, such as Disable or Modify System Firewall or tampering to enable Proxy. Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

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
- T1070.007: https://attack.mitre.org/techniques/T1070/007
- Reviewed: 2026-10-27
