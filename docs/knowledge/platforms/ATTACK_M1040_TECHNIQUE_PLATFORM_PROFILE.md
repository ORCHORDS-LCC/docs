# Behavior Prevention on Endpoint Technique Platform Profile

## Reference

- Technique: **M1040 — Behavior Prevention on Endpoint**
- Platforms named in the source: not stated

Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures: Suspicious Process Behavior: - Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior, such as privilege escalation attempts. - Use Case: An attacker uses a known vulnerability to spawn a privileged process from a user-level application. The endpoint tool detects the abnormal parent-child process relationship and blocks the action. Unauthorized File Access: - Implementation: Leverage Data Loss Prevention (DLP) or endpoint tools to block processes attempting to access sensitive files without proper authorization. - Use Case: A process tries to read or modify a sensitive file located in a restricted directory, such as /etc/shadow on Linux or the SAM registry hive on Windows. The endpoint tool identifies this anomalous behavior and prevents it. Abnormal API Calls: - Implementation: Implement runtime analysis tools to monitor API calls and block those associated with malicious activities. - Use Case: A process dynamically injects itself into another process to hijack its execution. The endpoint detects the abnormal use of APIs like `OpenProcess` and `WriteProcessMemory` and terminates the offending process. Exploit Prevention: - Implementation: Use behavioral exploit prevention tools to detect and block exploits attempting to gain unauthorized access. - Use Case: A buffer overflow exploit is launched against a vulnerable application. The endpoint detects the anomalous memory write operation and halts the process.

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
- M1040: https://attack.mitre.org/mitigations/M1040
- Reviewed: 2026-10-27
