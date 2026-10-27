# Service Creation Technique Operationalization Review

## Reference

- Technique: **DC0060 — Service Creation**

The registration of a new service or daemon on an operating system. *Data Collection Measures:* - Windows Event Logs - Event ID 4697 - Captures the creation of a new Windows service. - Event ID 7045 - Captures services installed by administrators or adversaries. - Event ID 7034 - Could indicate malicious service modification or exploitation. - Sysmon Logs - Sysmon Event ID 1 - Process Creation (captures service executables). - Sysmon Event ID 4 - Service state changes (detects service installation). - Sysmon Event ID 13 - Registry modifications (captures service persistence changes). - PowerShell Logging - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script Block Logging). - Linux/macOS Collection Methods - AuditD & Syslog Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`) - AuditD Rules: - `auditctl -w /etc/systemd/system -p wa -k service_creation` - Detects changes to `systemd` service configurations. - Systemd Journals (`journalctl -u <service_name>`) - Captures newly created systemd services. - LaunchDaemons & LaunchAgents (macOS) - Monitor `/Library/LaunchDaemons/` and `/Library/LaunchAgents/` for new plist files.

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
- DC0060: https://attack.mitre.org/datacomponents/DC0060
- Reviewed: 2026-10-27
