# T1562.003 Impair Command History Logging Outcome Lesson

## Authoritative description

- Technique: **T1562.003 — Impair Command History Logging**
- Tactics: stealth
- Platforms: ESXi, Linux, macOS, Network Devices, Windows

Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done. On Linux and macOS, command history is tracked in a file pointed to by the environment variable HISTFILE. When a user logs off a system, this information is flushed to a file in the user's home directory called ~/.bash_history. The HISTCONTROL environment variable keeps track of what should be saved by the history command and eventually into the ~/.bash_history file when a user logs out. HISTCONTROL does not exist by default on macOS, but can be set by the user and will be respected. The `HISTFILE` environment variable is also used in some ESXi systems. Adversaries may clear the history environment variable (unset HISTFILE) or set the command history size to zero (export HISTFILESIZE=0) to prevent logging of commands. Additionally, HISTCONTROL can be configured to ignore commands that start with a space by simply setting it to "ignorespace". HISTCONTROL can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that “ ls” will not be saved, but “ls” would be saved by history. Adversaries can abuse this to operate without leaving traces by simply prepending a space to all of their terminal commands. On Windows systems, the PSReadLine module tracks commands used in all PowerShell sessions and writes them to a file ($env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt by default). Adversaries may change where these logs are saved using Set-PSReadLineOption -HistorySavePath {File Path}. This will cause ConsoleHost_history.txt to stop receiving logs. Additionally, it is possible to turn off logging to this file using the PowerShell command Set-PSReadlineOption -HistorySaveStyle SaveNothing. Adversaries may also leverage a Network Device CLI on network devices to disable historical command logging (e.g. no logging).

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
- T1562.003: https://attack.mitre.org/techniques/T1562/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
