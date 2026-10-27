# Process Access Technique Response Playbook

## Target technique

**DC0035 — Process Access**


Refers to an event where one process attempts to open another process, typically to inspect or manipulate its memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection. *Data Collection Measures:* - Endpoint Detection and Response (EDR) Tools: - EDR solutions that provide telemetry on inter-process access and memory manipulation. - Sysmon (Windows): - Event ID 10: Captures process access attempts, including: - Source process (initiator) - Target process (victim) - Access rights requested - Process ID correlation - Windows Event Logs: - Event ID 4656 (Audit Handle to an Object): Logs access attempts to system objects. - Event ID 4690 (Attempted Process Modification): Can help identify unauthorized process changes. - Linux/macOS Monitoring: - AuditD: Monitors process access through syscall tracing (e.g., `ptrace`, `open`, `read`, `write`). - eBPF/XDP: Used for low-level monitoring of kernel process access. - OSQuery: Query process access behavior via structured SQL-like logging. - Procmon (Process Monitor) and Debugging Tools: - Windows Procmon: Captures real-time process interactions. - Linux strace / ptrace: Useful for tracking process behavior at the system call level.

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
- DC0035: https://attack.mitre.org/datacomponents/DC0035
- Reviewed: 2026-10-27
