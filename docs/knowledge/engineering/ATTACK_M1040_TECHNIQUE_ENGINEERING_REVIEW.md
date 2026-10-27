# Behavior Prevention on Endpoint Technique Engineering Review

## Reference

- Technique: **M1040 — Behavior Prevention on Endpoint**

Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures: Suspicious Process Behavior: - Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior, such as privilege escalation attempts. - Use Case: An attacker uses a known vulnerability to spawn a privileged process from a user-level application. The endpoint tool detects the abnormal parent-child process relationship and blocks the action. Unauthorized File Access: - Implementation: Leverage Data Loss Prevention (DLP) or endpoint tools to block processes attempting to access sensitive files without proper authorization. - Use Case: A process tries to read or modify a sensitive file located in a restricted directory, such as /etc/shadow on Linux or the SAM registry hive on Windows. The endpoint tool identifies this anomalous behavior and prevents it. Abnormal API Calls: - Implementation: Implement runtime analysis tools to monitor API calls and block those associated with malicious activities. - Use Case: A process dynamically injects itself into another process to hijack its execution. The endpoint detects the abnormal use of APIs like `OpenProcess` and `WriteProcessMemory` and terminates the offending process. Exploit Prevention: - Implementation: Use behavioral exploit prevention tools to detect and block exploits attempting to gain unauthorized access. - Use Case: A buffer overflow exploit is launched against a vulnerable application. The endpoint detects the anomalous memory write operation and halts the process.

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
- M1040: https://attack.mitre.org/mitigations/M1040
- Reviewed: 2026-10-27
