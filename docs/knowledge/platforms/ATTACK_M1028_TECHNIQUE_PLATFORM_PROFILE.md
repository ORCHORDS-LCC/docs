# Operating System Configuration Technique Platform Profile

## Reference

- Technique: **M1028 — Operating System Configuration**
- Platforms named in the source: not stated

Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: Disable Unused Features: - Turn off SMBv1, LLMNR, and NetBIOS where not needed. - Disable remote registry and unnecessary services. Enforce OS-level Protections: - Enable Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG) on Windows. - Use AppArmor or SELinux on Linux for mandatory access controls. Secure Access Settings: - Enable User Account Control (UAC) for Windows. - Restrict root/sudo access on Linux/macOS and enforce strong permissions using sudoers files. File System Hardening: - Implement least-privilege access for critical files and system directories. - Audit permissions regularly using tools like icacls (Windows) or getfacl/chmod (Linux/macOS). Secure Remote Access: - Restrict RDP, SSH, and VNC to authorized IPs using firewall rules. - Enable NLA for RDP and enforce strong password/lockout policies. Harden Boot Configurations: - Enable Secure Boot and enforce UEFI/BIOS password protection. - Use BitLocker or LUKS to encrypt boot drives. Regular Audits: - Periodically audit OS configurations using tools like CIS Benchmarks or SCAP tools. *Tools for Implementation* Windows: - Microsoft Group Policy Objects (GPO): Centrally enforce OS security settings. - Windows Defender Exploit Guard: Built-in OS protection against exploits. - CIS-CAT Pro: Audit Windows security configurations based on CIS Benchmarks. Linux/macOS: - AppArmor/SELinux: Enforce mandatory access controls. - Lynis: Perform comprehensive security audits. - SCAP Security Guide: Automate configuration hardening using Security Content Automation Protocol. Cross-Platform: - Ansible or Chef/Puppet: Automate configuration hardening at scale. - OpenSCAP: Perform compliance and configuration checks.

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
- M1028: https://attack.mitre.org/mitigations/M1028
- Reviewed: 2026-10-27
