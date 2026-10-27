# Operating System Configuration Technique Operationalization Review

## Reference

- Technique: **M1028 — Operating System Configuration**

Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: Disable Unused Features: - Turn off SMBv1, LLMNR, and NetBIOS where not needed. - Disable remote registry and unnecessary services. Enforce OS-level Protections: - Enable Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG) on Windows. - Use AppArmor or SELinux on Linux for mandatory access controls. Secure Access Settings: - Enable User Account Control (UAC) for Windows. - Restrict root/sudo access on Linux/macOS and enforce strong permissions using sudoers files. File System Hardening: - Implement least-privilege access for critical files and system directories. - Audit permissions regularly using tools like icacls (Windows) or getfacl/chmod (Linux/macOS). Secure Remote Access: - Restrict RDP, SSH, and VNC to authorized IPs using firewall rules. - Enable NLA for RDP and enforce strong password/lockout policies. Harden Boot Configurations: - Enable Secure Boot and enforce UEFI/BIOS password protection. - Use BitLocker or LUKS to encrypt boot drives. Regular Audits: - Periodically audit OS configurations using tools like CIS Benchmarks or SCAP tools. *Tools for Implementation* Windows: - Microsoft Group Policy Objects (GPO): Centrally enforce OS security settings. - Windows Defender Exploit Guard: Built-in OS protection against exploits. - CIS-CAT Pro: Audit Windows security configurations based on CIS Benchmarks. Linux/macOS: - AppArmor/SELinux: Enforce mandatory access controls. - Lynis: Perform comprehensive security audits. - SCAP Security Guide: Automate configuration hardening using Security Content Automation Protocol. Cross-Platform: - Ansible or Chef/Puppet: Automate configuration hardening at scale. - OpenSCAP: Perform compliance and configuration checks.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1028: https://attack.mitre.org/mitigations/M1028
- Reviewed: 2026-10-27
