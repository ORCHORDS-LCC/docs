# Exploit Protection Technique Platform Profile

## Reference

- Technique: **M1050 — Exploit Protection**
- Platforms named in the source: not stated

Deploy capabilities that detect, block, and mitigate conditions indicative of software exploits. These capabilities aim to prevent exploitation by addressing vulnerabilities, monitoring anomalous behaviors, and applying exploit-mitigation techniques to harden systems and software. Operating System Exploit Protections: - Use Case: Enable built-in exploit protection features provided by modern operating systems, such as Microsoft's Exploit Protection, which includes techniques like Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG). - Implementation: Enforce DEP for all programs and enable ASLR to randomize memory addresses used by system and application processes. Windows: Configure Exploit Protection through the Windows Security app or deploy settings via Group Policy. `ExploitProtectionExportSettings.exe -path "exploit_settings.xml"` Linux: Use Kernel-level hardening features like SELinux, AppArmor, or GRSEC to enforce memory protections and prevent exploits. Third-Party Endpoint Security: - Use Case: Use endpoint protection tools with built-in exploit protection, such as enhanced memory protection, behavior monitoring, and real-time exploit detection. - Implementation: Deploy tools to detect and block exploitation attempts targeting unpatched software. Virtual Patching: - Use Case: Use tools to implement virtual patches that mitigate vulnerabilities in applications or operating systems until official patches are applied. - Implementation: Use Intrusion Prevention System (IPS) to block exploitation attempts on known vulnerabilities in outdated applications. Hardening Application Configurations: - Use Case: Disable risky application features that can be exploited, such as macros in Microsoft Office or JScript in Internet Explorer. - Implementation: Configure Microsoft Office Group Policies to disable execution of macros in downloaded files.

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
- M1050: https://attack.mitre.org/mitigations/M1050
- Reviewed: 2026-10-27
