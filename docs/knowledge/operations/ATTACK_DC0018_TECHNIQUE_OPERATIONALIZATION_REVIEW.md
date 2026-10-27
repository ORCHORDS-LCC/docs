# Host Status Technique Operationalization Review

## Reference

- Technique: **DC0018 — Host Status**

Logging, messaging, and other artifacts that highlight the health and operational state of host-based security sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate security control evasion by adversaries. *Data Collection Measures:* - Windows Event Logs: - Event ID 1074 (System Shutdown): Detects unexpected system reboots/shutdowns. - Event ID 6006 (Event Log Stopped): Logs when Windows event logging is stopped. - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering. - Event ID 12 (Windows Defender Status Change) – Detects changes in Windows Defender state. - Linux/macOS Monitoring: - `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log` - Journald (journalctl) for kernel and system alerts. - Endpoint Detection and Response (EDR) Tools: - Monitor agent health status, detect sensor tampering, and alert on missing telemetry. - Mobile Threat Intelligence Logs: - Samsung Knox, SafetyNet, iOS Secure Enclave provide sensor health status for mobile endpoints.

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
- DC0018: https://attack.mitre.org/datacomponents/DC0018
- Reviewed: 2026-10-27
