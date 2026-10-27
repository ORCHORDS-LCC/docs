# Ignore Process Interrupts Technique Engineering Review

## Reference

- Technique: **T1564.011 — Ignore Process Interrupts**

Adversaries may evade defensive mechanisms by executing commands that hide from process interrupt signals. Many operating systems use signals to deliver messages to control process behavior. Command interpreters often include specific commands/flags that ignore errors and other hangups, such as when the user of the active session logs off. These interrupt signals may also be used by defensive tools and/or analysts to pause or terminate specified running processes. Adversaries may invoke processes using `nohup`, PowerShell `-ErrorAction SilentlyContinue`, or similar commands that may be immune to hangups. This may enable malicious commands and malware to continue execution through system events that would otherwise terminate its execution, such as users logging off or the termination of its C2 network connection. Hiding from process interrupt signals may allow malware to continue execution, but unlike Trap this does not establish Persistence since the process will not be re-invoked once actually terminated.

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
- T1564.011: https://attack.mitre.org/techniques/T1564/011
- Reviewed: 2026-10-27
