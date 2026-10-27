# Named Pipe Metadata Technique Engineering Review

## Reference

- Technique: **DC0048 — Named Pipe Metadata**

Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18) *Data Collection Measures:* - Windows: - Sysmon Event ID 17: Logs the creation of a named pipe. - Sysmon Event ID 18: Logs connection attempts to a named pipe. - Windows Security Event ID 5145: Logs access attempts to named pipes via SMB shares. - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions. - Linux/macOS: - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage. - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes. - Strace (`strace -e open <process>`): Monitors named pipe interactions. - Endpoint Detection & Response (EDR): - Capture named pipe events as part of process tracking. - Memory Forensics: - Volatility Plugin (`pipescan`): Enumerates named pipes in system memory. - Rekall Framework: Identifies active named pipes and associated processes.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0048: https://attack.mitre.org/datacomponents/DC0048
- Reviewed: 2026-10-27
