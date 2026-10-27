# Antivirus/Antimalware Technique Platform Profile

## Reference

- Technique: **M1049 — Antivirus/Antimalware**
- Platforms named in the source: not stated

Antivirus/Antimalware solutions utilize signatures, heuristics, and behavioral analysis to detect, block, and remediate malicious software, including viruses, trojans, ransomware, and spyware. These solutions continuously monitor endpoints and systems for known malicious patterns and suspicious behaviors that indicate compromise. Antivirus/Antimalware software should be deployed across all devices, with automated updates to ensure protection against the latest threats. This mitigation can be implemented through the following measures: Signature-Based Detection: - Implementation: Use predefined signatures to identify known malware based on unique patterns such as file hashes, byte sequences, or command-line arguments. This method is effective against known threats. - Use Case: When malware like "Emotet" is detected, its signature (such as a specific file hash) matches a known database of malicious software, triggering an alert and allowing immediate quarantine of the infected file. Heuristic-Based Detection: - Implementation: Deploy heuristic algorithms that analyze behavior and characteristics of files and processes to identify potential malware, even if it doesn’t match a known signature. - Use Case: If a program attempts to modify multiple critical system files or initiate suspicious network communications, heuristic analysis may flag it as potentially malicious, even if no specific malware signature is available. Behavioral Detection (Behavior Prevention): - Implementation: Use behavioral analysis to detect patterns of abnormal activities, such as unusual system calls, unauthorized file encryption, or attempts to escalate privileges. - Use Case: Behavioral analysis can detect ransomware attacks early by identifying behavior like mass file encryption, even before a specific ransomware signature has been identified. Real-Time Scanning: - Implementation: Enable real-time scanning to automatically inspect files and network traffic for signs of malware as they are accessed, downloaded, or executed. - Use Case: When a user downloads an email attachment, the antivirus solution scans the file in real-time, checking it against both signatures and heuristics to detect any malicious content before it can be opened. Cloud-Assisted Threat Intelligence: - Implementation: Use cloud-based threat intelligence to ensure the antivirus solution can access the latest malware definitions and real-time threat feeds from a global database of emerging threats. - Use Case: Cloud-assisted antivirus solutions quickly identify newly discovered malware by cross-referencing against global threat databases, providing real-time protection against zero-day attacks. **Tools for Implementation**: - Endpoint Security Platforms: Use solutions such as EDR for comprehensive antivirus/antimalware protection across all systems. - Centralized Management: Implement centralized antivirus management consoles that provide visibility into threat activity, enable policy enforcement, and automate updates. - Behavioral Analysis Tools: Leverage solutions with advanced behavioral analysis capabilities to detect malicious activity patterns that don’t rely on known signatures.

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
- M1049: https://attack.mitre.org/mitigations/M1049
- Reviewed: 2026-10-27
