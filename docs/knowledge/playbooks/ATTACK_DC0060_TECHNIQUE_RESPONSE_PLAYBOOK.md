# Service Creation Technique Response Playbook

## Target technique

**DC0060 — Service Creation**


The registration of a new service or daemon on an operating system. *Data Collection Measures:* - Windows Event Logs - Event ID 4697 - Captures the creation of a new Windows service. - Event ID 7045 - Captures services installed by administrators or adversaries. - Event ID 7034 - Could indicate malicious service modification or exploitation. - Sysmon Logs - Sysmon Event ID 1 - Process Creation (captures service executables). - Sysmon Event ID 4 - Service state changes (detects service installation). - Sysmon Event ID 13 - Registry modifications (captures service persistence changes). - PowerShell Logging - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script Block Logging). - Linux/macOS Collection Methods - AuditD & Syslog Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`) - AuditD Rules: - `auditctl -w /etc/systemd/system -p wa -k service_creation` - Detects changes to `systemd` service configurations. - Systemd Journals (`journalctl -u <service_name>`) - Captures newly created systemd services. - LaunchDaemons & LaunchAgents (macOS) - Monitor `/Library/LaunchDaemons/` and `/Library/LaunchAgents/` for new plist files.

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
- DC0060: https://attack.mitre.org/datacomponents/DC0060
- Reviewed: 2026-10-27
