# Process Access Technique Engineering Review

## Reference

- Technique: **DC0035 — Process Access**

Refers to an event where one process attempts to open another process, typically to inspect or manipulate its memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection. *Data Collection Measures:* - Endpoint Detection and Response (EDR) Tools: - EDR solutions that provide telemetry on inter-process access and memory manipulation. - Sysmon (Windows): - Event ID 10: Captures process access attempts, including: - Source process (initiator) - Target process (victim) - Access rights requested - Process ID correlation - Windows Event Logs: - Event ID 4656 (Audit Handle to an Object): Logs access attempts to system objects. - Event ID 4690 (Attempted Process Modification): Can help identify unauthorized process changes. - Linux/macOS Monitoring: - AuditD: Monitors process access through syscall tracing (e.g., `ptrace`, `open`, `read`, `write`). - eBPF/XDP: Used for low-level monitoring of kernel process access. - OSQuery: Query process access behavior via structured SQL-like logging. - Procmon (Process Monitor) and Debugging Tools: - Windows Procmon: Captures real-time process interactions. - Linux strace / ptrace: Useful for tracking process behavior at the system call level.

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
- DC0035: https://attack.mitre.org/datacomponents/DC0035
- Reviewed: 2026-10-27
