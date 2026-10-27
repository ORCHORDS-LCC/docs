# Shell History Technique Response Playbook

## Target technique

**T1552.003 — Shell History**

- Tactics: credential-access
- Platforms: Linux, macOS, Windows

Adversaries may search the command history on compromised systems for insecurely stored credentials. On Linux and macOS systems, shells such as Bash and Zsh keep track of the commands users type on the command-line with the "history" utility. Once a user logs out, the history is flushed to the user's history file. For each user, this file resides at the same location: for example, `~/.bash_history` or `~/.zsh_history`. Typically, these files keeps track of the user's last 1000 commands. On Windows, PowerShell has both a command history that is wiped after the session ends, and one that contains commands used in all sessions and is persistent. The default location for persistent history can be found in `%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`, but command history can also be accessed with `Get-History`. Command Prompt (CMD) on Windows does not have persistent history. Users often type usernames and passwords on the command-line as parameters to programs, which then get saved to this file when they log out. Adversaries can abuse this by looking through the file for potential credentials.

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
- T1552.003: https://attack.mitre.org/techniques/T1552/003
- Reviewed: 2026-10-27
