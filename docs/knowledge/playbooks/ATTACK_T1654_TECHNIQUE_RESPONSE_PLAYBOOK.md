# Log Enumeration Technique Response Playbook

## Target technique

**T1654 — Log Enumeration**

- Tactics: discovery
- Platforms: ESXi, IaaS, Linux, macOS, Windows

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records (Account Discovery), security or vulnerable software (Software Discovery), or hosts within a compromised network (Remote System Discovery). Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or PowerShell on Windows to access and/or export security event information. In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure. Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis. In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.

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
- T1654: https://attack.mitre.org/techniques/T1654
- Reviewed: 2026-10-27
