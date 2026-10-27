# Process Access Technique Platform Profile

## Reference

- Technique: **DC0035 — Process Access**
- Platforms named in the source: not stated

Refers to an event where one process attempts to open another process, typically to inspect or manipulate its memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection. *Data Collection Measures:* - Endpoint Detection and Response (EDR) Tools: - EDR solutions that provide telemetry on inter-process access and memory manipulation. - Sysmon (Windows): - Event ID 10: Captures process access attempts, including: - Source process (initiator) - Target process (victim) - Access rights requested - Process ID correlation - Windows Event Logs: - Event ID 4656 (Audit Handle to an Object): Logs access attempts to system objects. - Event ID 4690 (Attempted Process Modification): Can help identify unauthorized process changes. - Linux/macOS Monitoring: - AuditD: Monitors process access through syscall tracing (e.g., `ptrace`, `open`, `read`, `write`). - eBPF/XDP: Used for low-level monitoring of kernel process access. - OSQuery: Query process access behavior via structured SQL-like logging. - Procmon (Process Monitor) and Debugging Tools: - Windows Procmon: Captures real-time process interactions. - Linux strace / ptrace: Useful for tracking process behavior at the system call level.

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
- DC0035: https://attack.mitre.org/datacomponents/DC0035
- Reviewed: 2026-10-27
