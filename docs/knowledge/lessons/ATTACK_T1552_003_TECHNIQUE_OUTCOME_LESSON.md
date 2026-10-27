# T1552.003 Shell History Outcome Lesson

## Authoritative description

- Technique: **T1552.003 — Shell History**
- Tactics: credential-access
- Platforms: Linux, macOS, Windows

Adversaries may search the command history on compromised systems for insecurely stored credentials. On Linux and macOS systems, shells such as Bash and Zsh keep track of the commands users type on the command-line with the "history" utility. Once a user logs out, the history is flushed to the user's history file. For each user, this file resides at the same location: for example, `~/.bash_history` or `~/.zsh_history`. Typically, these files keeps track of the user's last 1000 commands. On Windows, PowerShell has both a command history that is wiped after the session ends, and one that contains commands used in all sessions and is persistent. The default location for persistent history can be found in `%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`, but command history can also be accessed with `Get-History`. Command Prompt (CMD) on Windows does not have persistent history. Users often type usernames and passwords on the command-line as parameters to programs, which then get saved to this file when they log out. Adversaries can abuse this by looking through the file for potential credentials.

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
- T1552.003: https://attack.mitre.org/techniques/T1552/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
