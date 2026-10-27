# Service Creation Technique Platform Profile

## Reference

- Technique: **DC0060 — Service Creation**
- Platforms named in the source: not stated

The registration of a new service or daemon on an operating system. *Data Collection Measures:* - Windows Event Logs - Event ID 4697 - Captures the creation of a new Windows service. - Event ID 7045 - Captures services installed by administrators or adversaries. - Event ID 7034 - Could indicate malicious service modification or exploitation. - Sysmon Logs - Sysmon Event ID 1 - Process Creation (captures service executables). - Sysmon Event ID 4 - Service state changes (detects service installation). - Sysmon Event ID 13 - Registry modifications (captures service persistence changes). - PowerShell Logging - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script Block Logging). - Linux/macOS Collection Methods - AuditD & Syslog Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`) - AuditD Rules: - `auditctl -w /etc/systemd/system -p wa -k service_creation` - Detects changes to `systemd` service configurations. - Systemd Journals (`journalctl -u <service_name>`) - Captures newly created systemd services. - LaunchDaemons & LaunchAgents (macOS) - Monitor `/Library/LaunchDaemons/` and `/Library/LaunchAgents/` for new plist files.

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
- DC0060: https://attack.mitre.org/datacomponents/DC0060
- Reviewed: 2026-10-27
