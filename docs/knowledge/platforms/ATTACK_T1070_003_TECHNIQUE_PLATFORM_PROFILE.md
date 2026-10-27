# Clear Command History Technique Platform Profile

## Reference

- Technique: **T1070.003 — Clear Command History**
- Platforms named in the source: ESXi, Linux, macOS, Network Devices, Windows

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done. On Linux and macOS, these command histories can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable HISTFILE. When a user logs off a system, this information is flushed to a file in the user's home directory called ~/.bash_history. The benefit of this is that it allows users to go back to commands they've used before in different sessions. Adversaries may delete their commands from these logs by manually clearing the history (history -c) or deleting the bash history file rm ~/.bash_history. Adversaries may also leverage a Network Device CLI on network devices to clear command history data (clear logging and/or clear history). On ESXi servers, command history may be manually removed from the `/var/log/shell.log` file. On Windows hosts, PowerShell has two different command history providers: the built-in history and the command history managed by the PSReadLine module. The built-in history only tracks the commands used in the current session. This command history is not available to other sessions and is deleted when the session ends. The PSReadLine command history tracks the commands used in all PowerShell sessions and writes them to a file ($env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt by default). This history file is available to all sessions and contains all past history since the file is not deleted when the session ends. Adversaries may run the PowerShell command Clear-History to flush the entire command history from a current PowerShell session. This, however, will not delete/flush the ConsoleHost_history.txt file. Adversaries may also delete the ConsoleHost_history.txt file or edit its contents to hide PowerShell commands they have run.

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
- T1070.003: https://attack.mitre.org/techniques/T1070/003
- Reviewed: 2026-10-27
