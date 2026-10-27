# Clear Command History Technique Response Playbook

## Target technique

**T1070.003 — Clear Command History**

- Tactics: stealth
- Platforms: ESXi, Linux, macOS, Network Devices, Windows

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done. On Linux and macOS, these command histories can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable HISTFILE. When a user logs off a system, this information is flushed to a file in the user's home directory called ~/.bash_history. The benefit of this is that it allows users to go back to commands they've used before in different sessions. Adversaries may delete their commands from these logs by manually clearing the history (history -c) or deleting the bash history file rm ~/.bash_history. Adversaries may also leverage a Network Device CLI on network devices to clear command history data (clear logging and/or clear history). On ESXi servers, command history may be manually removed from the `/var/log/shell.log` file. On Windows hosts, PowerShell has two different command history providers: the built-in history and the command history managed by the PSReadLine module. The built-in history only tracks the commands used in the current session. This command history is not available to other sessions and is deleted when the session ends. The PSReadLine command history tracks the commands used in all PowerShell sessions and writes them to a file ($env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt by default). This history file is available to all sessions and contains all past history since the file is not deleted when the session ends. Adversaries may run the PowerShell command Clear-History to flush the entire command history from a current PowerShell session. This, however, will not delete/flush the ConsoleHost_history.txt file. Adversaries may also delete the ConsoleHost_history.txt file or edit its contents to hide PowerShell commands they have run.

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
- T1070.003: https://attack.mitre.org/techniques/T1070/003
- Reviewed: 2026-10-27
