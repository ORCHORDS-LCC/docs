# Named Pipe Metadata Technique Platform Profile

## Reference

- Technique: **DC0048 — Named Pipe Metadata**
- Platforms named in the source: not stated

Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18) *Data Collection Measures:* - Windows: - Sysmon Event ID 17: Logs the creation of a named pipe. - Sysmon Event ID 18: Logs connection attempts to a named pipe. - Windows Security Event ID 5145: Logs access attempts to named pipes via SMB shares. - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions. - Linux/macOS: - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage. - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes. - Strace (`strace -e open <process>`): Monitors named pipe interactions. - Endpoint Detection & Response (EDR): - Capture named pipe events as part of process tracking. - Memory Forensics: - Volatility Plugin (`pipescan`): Enumerates named pipes in system memory. - Rekall Framework: Identifies active named pipes and associated processes.

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
- DC0048: https://attack.mitre.org/datacomponents/DC0048
- Reviewed: 2026-10-27
