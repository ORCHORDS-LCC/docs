# Behavior Prevention on Endpoint Technique Response Playbook

## Target technique

**M1040 — Behavior Prevention on Endpoint**


Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures: Suspicious Process Behavior: - Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior, such as privilege escalation attempts. - Use Case: An attacker uses a known vulnerability to spawn a privileged process from a user-level application. The endpoint tool detects the abnormal parent-child process relationship and blocks the action. Unauthorized File Access: - Implementation: Leverage Data Loss Prevention (DLP) or endpoint tools to block processes attempting to access sensitive files without proper authorization. - Use Case: A process tries to read or modify a sensitive file located in a restricted directory, such as /etc/shadow on Linux or the SAM registry hive on Windows. The endpoint tool identifies this anomalous behavior and prevents it. Abnormal API Calls: - Implementation: Implement runtime analysis tools to monitor API calls and block those associated with malicious activities. - Use Case: A process dynamically injects itself into another process to hijack its execution. The endpoint detects the abnormal use of APIs like `OpenProcess` and `WriteProcessMemory` and terminates the offending process. Exploit Prevention: - Implementation: Use behavioral exploit prevention tools to detect and block exploits attempting to gain unauthorized access. - Use Case: A buffer overflow exploit is launched against a vulnerable application. The endpoint detects the anomalous memory write operation and halts the process.

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
- M1040: https://attack.mitre.org/mitigations/M1040
- Reviewed: 2026-10-27
