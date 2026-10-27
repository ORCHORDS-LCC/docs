# Command Execution Technique Platform Profile

## Reference

- Technique: **DC0064 — Command Execution**
- Platforms named in the source: not stated

Command Execution involves monitoring and capturing the execution of textual commands (including shell commands, cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution. Examples: - Windows Command Prompt - dir – Lists directory contents. - net user – Queries or manipulates user accounts. - tasklist – Lists running processes. - PowerShell - Get-Process – Retrieves processes running on a system. - Set-ExecutionPolicy – Changes PowerShell script execution policies. - Invoke-WebRequest – Downloads remote resources. - Linux Shell - ls – Lists files in a directory. - cat /etc/passwd – Reads the user accounts file. - curl http://malicious-site.com – Retrieves content from a malicious URL. - Container Environments - docker exec – Executes a command inside a running container. - kubectl exec – Runs commands in Kubernetes pods. - macOS Terminal - open – Opens files or URLs. - dscl . -list /Users – Lists all users on the system. - osascript -e – Executes AppleScript commands.

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
- DC0064: https://attack.mitre.org/datacomponents/DC0064
- Reviewed: 2026-10-27
