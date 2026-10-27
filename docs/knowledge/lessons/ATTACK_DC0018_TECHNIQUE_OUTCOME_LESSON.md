# DC0018 Host Status Outcome Lesson

## Authoritative description

- Technique: **DC0018 — Host Status**

Logging, messaging, and other artifacts that highlight the health and operational state of host-based security sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate security control evasion by adversaries. *Data Collection Measures:* - Windows Event Logs: - Event ID 1074 (System Shutdown): Detects unexpected system reboots/shutdowns. - Event ID 6006 (Event Log Stopped): Logs when Windows event logging is stopped. - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering. - Event ID 12 (Windows Defender Status Change) – Detects changes in Windows Defender state. - Linux/macOS Monitoring: - `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log` - Journald (journalctl) for kernel and system alerts. - Endpoint Detection and Response (EDR) Tools: - Monitor agent health status, detect sensor tampering, and alert on missing telemetry. - Mobile Threat Intelligence Logs: - Samsung Knox, SafetyNet, iOS Secure Enclave provide sensor health status for mobile endpoints.

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
- DC0018: https://attack.mitre.org/datacomponents/DC0018
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
