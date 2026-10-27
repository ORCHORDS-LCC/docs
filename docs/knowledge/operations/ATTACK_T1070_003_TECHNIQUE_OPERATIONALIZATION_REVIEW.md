# Clear Command History Technique Operationalization Review

## Reference

- Technique: **T1070.003 — Clear Command History**

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done. On Linux and macOS, these command histories can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable HISTFILE. When a user logs off a system, this information is flushed to a file in the user's home directory called ~/.bash_history. The benefit of this is that it allows users to go back to commands they've used before in different sessions. Adversaries may delete their commands from these logs by manually clearing the history (history -c) or deleting the bash history file rm ~/.bash_history. Adversaries may also leverage a Network Device CLI on network devices to clear command history data (clear logging and/or clear history). On ESXi servers, command history may be manually removed from the `/var/log/shell.log` file. On Windows hosts, PowerShell has two different command history providers: the built-in history and the command history managed by the PSReadLine module. The built-in history only tracks the commands used in the current session. This command history is not available to other sessions and is deleted when the session ends. The PSReadLine command history tracks the commands used in all PowerShell sessions and writes them to a file ($env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt by default). This history file is available to all sessions and contains all past history since the file is not deleted when the session ends. Adversaries may run the PowerShell command Clear-History to flush the entire command history from a current PowerShell session. This, however, will not delete/flush the ConsoleHost_history.txt file. Adversaries may also delete the ConsoleHost_history.txt file or edit its contents to hide PowerShell commands they have run.

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
- T1070.003: https://attack.mitre.org/techniques/T1070/003
- Reviewed: 2026-10-27
