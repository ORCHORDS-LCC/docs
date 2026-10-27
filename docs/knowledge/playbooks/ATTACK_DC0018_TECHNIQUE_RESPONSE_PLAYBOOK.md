# Host Status Technique Response Playbook

## Target technique

**DC0018 — Host Status**


Logging, messaging, and other artifacts that highlight the health and operational state of host-based security sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate security control evasion by adversaries. *Data Collection Measures:* - Windows Event Logs: - Event ID 1074 (System Shutdown): Detects unexpected system reboots/shutdowns. - Event ID 6006 (Event Log Stopped): Logs when Windows event logging is stopped. - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering. - Event ID 12 (Windows Defender Status Change) – Detects changes in Windows Defender state. - Linux/macOS Monitoring: - `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log` - Journald (journalctl) for kernel and system alerts. - Endpoint Detection and Response (EDR) Tools: - Monitor agent health status, detect sensor tampering, and alert on missing telemetry. - Mobile Threat Intelligence Logs: - Samsung Knox, SafetyNet, iOS Secure Enclave provide sensor health status for mobile endpoints.

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
- DC0018: https://attack.mitre.org/datacomponents/DC0018
- Reviewed: 2026-10-27
