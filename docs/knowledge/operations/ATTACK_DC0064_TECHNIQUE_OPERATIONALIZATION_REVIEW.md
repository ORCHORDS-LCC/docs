# Command Execution Technique Operationalization Review

## Reference

- Technique: **DC0064 — Command Execution**

Command Execution involves monitoring and capturing the execution of textual commands (including shell commands, cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution. Examples: - Windows Command Prompt - dir – Lists directory contents. - net user – Queries or manipulates user accounts. - tasklist – Lists running processes. - PowerShell - Get-Process – Retrieves processes running on a system. - Set-ExecutionPolicy – Changes PowerShell script execution policies. - Invoke-WebRequest – Downloads remote resources. - Linux Shell - ls – Lists files in a directory. - cat /etc/passwd – Reads the user accounts file. - curl http://malicious-site.com – Retrieves content from a malicious URL. - Container Environments - docker exec – Executes a command inside a running container. - kubectl exec – Runs commands in Kubernetes pods. - macOS Terminal - open – Opens files or URLs. - dscl . -list /Users – Lists all users on the system. - osascript -e – Executes AppleScript commands.

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
- DC0064: https://attack.mitre.org/datacomponents/DC0064
- Reviewed: 2026-10-27
