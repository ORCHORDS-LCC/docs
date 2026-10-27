# Impair Command History Logging Technique Platform Profile

## Reference

- Technique: **T1562.003 — Impair Command History Logging**
- Platforms named in the source: ESXi, Linux, macOS, Network Devices, Windows

Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done. On Linux and macOS, command history is tracked in a file pointed to by the environment variable <code>HISTFILE</code>. When a user logs off a system, this information is flushed to a file in the user's home directory called <code>~/.bash_history</code>. The <code>HISTCONTROL</code> environment variable keeps track of what should be saved by the <code>history</code> command and eventually into the <code>~/.bash_history</code> file when a user logs out. <code>HISTCONTROL</code> does not exist by default on macOS, but can be set by the user and will be respected. The `HISTFILE` environment variable is also used in some ESXi systems. Adversaries may clear the history environment variable (<code>unset HISTFILE</code>) or set the command history size to zero (<code>export HISTFILESIZE=0</code>) to prevent logging of commands. Additionally, <code>HISTCONTROL</code> can be configured to ignore commands that start with a space by simply setting it to "ignorespace". <code>HISTCONTROL</code> can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that “ ls” will not be saved, but “ls” would be saved by history. Adversaries can abuse this to operate without leaving traces by simply prepending a space to all of their terminal commands. On Windows systems, the <code>PSReadLine</code> module tracks commands used in all PowerShell sessions and writes them to a file (<code>$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt</code> by default). Adversaries may change where these logs are saved using <code>Set-PSReadLineOption -HistorySavePath {File Path}</code>. This will cause <code>ConsoleHost_history.txt</code> to stop receiving logs. Additionally, it is possible to turn off logging to this file using the PowerShell command <code>Set-PSReadlineOption -HistorySaveStyle SaveNothing</code>. Adversaries may also leverage a Network Device CLI on network devices to disable historical command logging (e.g. <code>no logging</code>).

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
- T1562.003: https://attack.mitre.org/techniques/T1562/003
- Reviewed: 2026-10-27
