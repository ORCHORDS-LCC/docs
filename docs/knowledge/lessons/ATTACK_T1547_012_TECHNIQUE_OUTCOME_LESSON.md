# T1547.012 Print Processors Outcome Lesson

## Authoritative description

- Technique: **T1547.012 — Print Processors**
- Tactics: persistence, privilege-escalation
- Platforms: Windows

Adversaries may abuse print processors to run malicious DLLs during system boot for persistence and/or privilege escalation. Print processors are DLLs that are loaded by the print spooler service, `spoolsv.exe`, during boot. Adversaries may abuse the print spooler service by adding print processors that load malicious DLLs at startup. A print processor can be installed through the AddPrintProcessor API call with an account that has SeLoadDriverPrivilege enabled. Alternatively, a print processor can be registered to the print spooler service by adding the HKLM\SYSTEM\\[CurrentControlSet or ControlSet001]\Control\Print\Environments\\[Windows architecture: e.g., Windows x64]\Print Processors\\[user defined]\Driver Registry key that points to the DLL. For the malicious print processor to be correctly installed, the payload must be located in the dedicated system print-processor directory, that can be found with the GetPrintProcessorDirectory API call, or referenced via a relative path from this directory. After the print processors are installed, the print spooler service, which starts during boot, must be restarted in order for them to run. The print spooler service runs under SYSTEM level permissions, therefore print processors installed by an adversary may run under elevated privileges.

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
- T1547.012: https://attack.mitre.org/techniques/T1547/012
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
