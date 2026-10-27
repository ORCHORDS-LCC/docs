# Log Enumeration Technique Platform Profile

## Reference

- Technique: **T1654 — Log Enumeration**
- Platforms named in the source: ESXi, IaaS, Linux, macOS, Windows

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records (Account Discovery), security or vulnerable software (Software Discovery), or hosts within a compromised network (Remote System Discovery). Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or PowerShell on Windows to access and/or export security event information. In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure. Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis. In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.

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
- T1654: https://attack.mitre.org/techniques/T1654
- Reviewed: 2026-10-27
