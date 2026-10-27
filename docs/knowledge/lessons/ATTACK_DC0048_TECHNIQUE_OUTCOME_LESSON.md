# DC0048 Named Pipe Metadata Outcome Lesson

## Authoritative description

- Technique: **DC0048 — Named Pipe Metadata**

Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18) *Data Collection Measures:* - Windows: - Sysmon Event ID 17: Logs the creation of a named pipe. - Sysmon Event ID 18: Logs connection attempts to a named pipe. - Windows Security Event ID 5145: Logs access attempts to named pipes via SMB shares. - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions. - Linux/macOS: - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage. - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes. - Strace (`strace -e open <process>`): Monitors named pipe interactions. - Endpoint Detection & Response (EDR): - Capture named pipe events as part of process tracking. - Memory Forensics: - Volatility Plugin (`pipescan`): Enumerates named pipes in system memory. - Rekall Framework: Identifies active named pipes and associated processes.

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
- DC0048: https://attack.mitre.org/datacomponents/DC0048
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
