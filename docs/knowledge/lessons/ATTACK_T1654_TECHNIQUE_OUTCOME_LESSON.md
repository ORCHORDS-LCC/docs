# T1654 Log Enumeration Outcome Lesson

## Authoritative description

- Technique: **T1654 — Log Enumeration**
- Tactics: discovery
- Platforms: ESXi, IaaS, Linux, macOS, Windows

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records (Account Discovery), security or vulnerable software (Software Discovery), or hosts within a compromised network (Remote System Discovery). Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or PowerShell on Windows to access and/or export security event information. In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure. Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis. In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.

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
- T1654: https://attack.mitre.org/techniques/T1654
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
