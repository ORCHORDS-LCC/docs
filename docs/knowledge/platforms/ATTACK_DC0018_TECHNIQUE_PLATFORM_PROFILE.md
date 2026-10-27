# Host Status Technique Platform Profile

## Reference

- Technique: **DC0018 — Host Status**
- Platforms named in the source: not stated

Logging, messaging, and other artifacts that highlight the health and operational state of host-based security sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate security control evasion by adversaries. *Data Collection Measures:* - Windows Event Logs: - Event ID 1074 (System Shutdown): Detects unexpected system reboots/shutdowns. - Event ID 6006 (Event Log Stopped): Logs when Windows event logging is stopped. - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering. - Event ID 12 (Windows Defender Status Change) – Detects changes in Windows Defender state. - Linux/macOS Monitoring: - `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log` - Journald (journalctl) for kernel and system alerts. - Endpoint Detection and Response (EDR) Tools: - Monitor agent health status, detect sensor tampering, and alert on missing telemetry. - Mobile Threat Intelligence Logs: - Samsung Knox, SafetyNet, iOS Secure Enclave provide sensor health status for mobile endpoints.

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
- DC0018: https://attack.mitre.org/datacomponents/DC0018
- Reviewed: 2026-10-27
