# Impair Command History Logging Technique Engineering Review

## Reference

- Technique: **T1562.003 — Impair Command History Logging**

Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done. On Linux and macOS, command history is tracked in a file pointed to by the environment variable HISTFILE. When a user logs off a system, this information is flushed to a file in the user's home directory called ~/.bash_history. The HISTCONTROL environment variable keeps track of what should be saved by the history command and eventually into the ~/.bash_history file when a user logs out. HISTCONTROL does not exist by default on macOS, but can be set by the user and will be respected. The `HISTFILE` environment variable is also used in some ESXi systems. Adversaries may clear the history environment variable (unset HISTFILE) or set the command history size to zero (export HISTFILESIZE=0) to prevent logging of commands. Additionally, HISTCONTROL can be configured to ignore commands that start with a space by simply setting it to "ignorespace". HISTCONTROL can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that “ ls” will not be saved, but “ls” would be saved by history. Adversaries can abuse this to operate without leaving traces by simply prepending a space to all of their terminal commands. On Windows systems, the PSReadLine module tracks commands used in all PowerShell sessions and writes them to a file ($env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt by default). Adversaries may change where these logs are saved using Set-PSReadLineOption -HistorySavePath {File Path}. This will cause ConsoleHost_history.txt to stop receiving logs. Additionally, it is possible to turn off logging to this file using the PowerShell command Set-PSReadlineOption -HistorySaveStyle SaveNothing. Adversaries may also leverage a Network Device CLI on network devices to disable historical command logging (e.g. no logging).

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1562.003: https://attack.mitre.org/techniques/T1562/003
- Reviewed: 2026-10-27
