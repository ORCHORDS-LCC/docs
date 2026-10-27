# Named Pipe Metadata Technique Response Playbook

## Target technique

**DC0048 — Named Pipe Metadata**


Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18) *Data Collection Measures:* - Windows: - Sysmon Event ID 17: Logs the creation of a named pipe. - Sysmon Event ID 18: Logs connection attempts to a named pipe. - Windows Security Event ID 5145: Logs access attempts to named pipes via SMB shares. - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions. - Linux/macOS: - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage. - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes. - Strace (`strace -e open <process>`): Monitors named pipe interactions. - Endpoint Detection & Response (EDR): - Capture named pipe events as part of process tracking. - Memory Forensics: - Volatility Plugin (`pipescan`): Enumerates named pipes in system memory. - Rekall Framework: Identifies active named pipes and associated processes.

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
- DC0048: https://attack.mitre.org/datacomponents/DC0048
- Reviewed: 2026-10-27
