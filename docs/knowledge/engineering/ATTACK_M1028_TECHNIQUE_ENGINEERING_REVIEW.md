# Operating System Configuration Technique Engineering Review

## Reference

- Technique: **M1028 — Operating System Configuration**

Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: Disable Unused Features: - Turn off SMBv1, LLMNR, and NetBIOS where not needed. - Disable remote registry and unnecessary services. Enforce OS-level Protections: - Enable Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG) on Windows. - Use AppArmor or SELinux on Linux for mandatory access controls. Secure Access Settings: - Enable User Account Control (UAC) for Windows. - Restrict root/sudo access on Linux/macOS and enforce strong permissions using sudoers files. File System Hardening: - Implement least-privilege access for critical files and system directories. - Audit permissions regularly using tools like icacls (Windows) or getfacl/chmod (Linux/macOS). Secure Remote Access: - Restrict RDP, SSH, and VNC to authorized IPs using firewall rules. - Enable NLA for RDP and enforce strong password/lockout policies. Harden Boot Configurations: - Enable Secure Boot and enforce UEFI/BIOS password protection. - Use BitLocker or LUKS to encrypt boot drives. Regular Audits: - Periodically audit OS configurations using tools like CIS Benchmarks or SCAP tools. *Tools for Implementation* Windows: - Microsoft Group Policy Objects (GPO): Centrally enforce OS security settings. - Windows Defender Exploit Guard: Built-in OS protection against exploits. - CIS-CAT Pro: Audit Windows security configurations based on CIS Benchmarks. Linux/macOS: - AppArmor/SELinux: Enforce mandatory access controls. - Lynis: Perform comprehensive security audits. - SCAP Security Guide: Automate configuration hardening using Security Content Automation Protocol. Cross-Platform: - Ansible or Chef/Puppet: Automate configuration hardening at scale. - OpenSCAP: Perform compliance and configuration checks.

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
- M1028: https://attack.mitre.org/mitigations/M1028
- Reviewed: 2026-10-27
