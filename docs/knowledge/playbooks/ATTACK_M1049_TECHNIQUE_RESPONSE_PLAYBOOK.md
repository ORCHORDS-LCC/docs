# Antivirus/Antimalware Technique Response Playbook

## Target technique

**M1049 — Antivirus/Antimalware**


Antivirus/Antimalware solutions utilize signatures, heuristics, and behavioral analysis to detect, block, and remediate malicious software, including viruses, trojans, ransomware, and spyware. These solutions continuously monitor endpoints and systems for known malicious patterns and suspicious behaviors that indicate compromise. Antivirus/Antimalware software should be deployed across all devices, with automated updates to ensure protection against the latest threats. This mitigation can be implemented through the following measures: Signature-Based Detection: - Implementation: Use predefined signatures to identify known malware based on unique patterns such as file hashes, byte sequences, or command-line arguments. This method is effective against known threats. - Use Case: When malware like "Emotet" is detected, its signature (such as a specific file hash) matches a known database of malicious software, triggering an alert and allowing immediate quarantine of the infected file. Heuristic-Based Detection: - Implementation: Deploy heuristic algorithms that analyze behavior and characteristics of files and processes to identify potential malware, even if it doesn’t match a known signature. - Use Case: If a program attempts to modify multiple critical system files or initiate suspicious network communications, heuristic analysis may flag it as potentially malicious, even if no specific malware signature is available. Behavioral Detection (Behavior Prevention): - Implementation: Use behavioral analysis to detect patterns of abnormal activities, such as unusual system calls, unauthorized file encryption, or attempts to escalate privileges. - Use Case: Behavioral analysis can detect ransomware attacks early by identifying behavior like mass file encryption, even before a specific ransomware signature has been identified. Real-Time Scanning: - Implementation: Enable real-time scanning to automatically inspect files and network traffic for signs of malware as they are accessed, downloaded, or executed. - Use Case: When a user downloads an email attachment, the antivirus solution scans the file in real-time, checking it against both signatures and heuristics to detect any malicious content before it can be opened. Cloud-Assisted Threat Intelligence: - Implementation: Use cloud-based threat intelligence to ensure the antivirus solution can access the latest malware definitions and real-time threat feeds from a global database of emerging threats. - Use Case: Cloud-assisted antivirus solutions quickly identify newly discovered malware by cross-referencing against global threat databases, providing real-time protection against zero-day attacks. **Tools for Implementation**: - Endpoint Security Platforms: Use solutions such as EDR for comprehensive antivirus/antimalware protection across all systems. - Centralized Management: Implement centralized antivirus management consoles that provide visibility into threat activity, enable policy enforcement, and automate updates. - Behavioral Analysis Tools: Leverage solutions with advanced behavioral analysis capabilities to detect malicious activity patterns that don’t rely on known signatures.

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
- M1049: https://attack.mitre.org/mitigations/M1049
- Reviewed: 2026-10-27
