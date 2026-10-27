# DC0064 Command Execution Outcome Lesson

## Authoritative description

- Technique: **DC0064 — Command Execution**

Command Execution involves monitoring and capturing the execution of textual commands (including shell commands, cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution. Examples: - Windows Command Prompt - dir – Lists directory contents. - net user – Queries or manipulates user accounts. - tasklist – Lists running processes. - PowerShell - Get-Process – Retrieves processes running on a system. - Set-ExecutionPolicy – Changes PowerShell script execution policies. - Invoke-WebRequest – Downloads remote resources. - Linux Shell - ls – Lists files in a directory. - cat /etc/passwd – Reads the user accounts file. - curl http://malicious-site.com – Retrieves content from a malicious URL. - Container Environments - docker exec – Executes a command inside a running container. - kubectl exec – Runs commands in Kubernetes pods. - macOS Terminal - open – Opens files or URLs. - dscl . -list /Users – Lists all users on the system. - osascript -e – Executes AppleScript commands.

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
- DC0064: https://attack.mitre.org/datacomponents/DC0064
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
