# T1564.011 Ignore Process Interrupts Outcome Lesson

## Authoritative description

- Technique: **T1564.011 — Ignore Process Interrupts**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may evade defensive mechanisms by executing commands that hide from process interrupt signals. Many operating systems use signals to deliver messages to control process behavior. Command interpreters often include specific commands/flags that ignore errors and other hangups, such as when the user of the active session logs off. These interrupt signals may also be used by defensive tools and/or analysts to pause or terminate specified running processes. Adversaries may invoke processes using `nohup`, PowerShell `-ErrorAction SilentlyContinue`, or similar commands that may be immune to hangups. This may enable malicious commands and malware to continue execution through system events that would otherwise terminate its execution, such as users logging off or the termination of its C2 network connection. Hiding from process interrupt signals may allow malware to continue execution, but unlike Trap this does not establish Persistence since the process will not be re-invoked once actually terminated.

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
- T1564.011: https://attack.mitre.org/techniques/T1564/011
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
