# Ignore Process Interrupts Technique Platform Profile

## Reference

- Technique: **T1564.011 — Ignore Process Interrupts**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may evade defensive mechanisms by executing commands that hide from process interrupt signals. Many operating systems use signals to deliver messages to control process behavior. Command interpreters often include specific commands/flags that ignore errors and other hangups, such as when the user of the active session logs off. These interrupt signals may also be used by defensive tools and/or analysts to pause or terminate specified running processes. Adversaries may invoke processes using `nohup`, PowerShell `-ErrorAction SilentlyContinue`, or similar commands that may be immune to hangups. This may enable malicious commands and malware to continue execution through system events that would otherwise terminate its execution, such as users logging off or the termination of its C2 network connection. Hiding from process interrupt signals may allow malware to continue execution, but unlike Trap this does not establish Persistence since the process will not be re-invoked once actually terminated.

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
- T1564.011: https://attack.mitre.org/techniques/T1564/011
- Reviewed: 2026-10-27
