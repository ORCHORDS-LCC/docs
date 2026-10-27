# Operating System Configuration Technique Response Playbook

## Target technique

**M1028 — Operating System Configuration**


Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: Disable Unused Features: - Turn off SMBv1, LLMNR, and NetBIOS where not needed. - Disable remote registry and unnecessary services. Enforce OS-level Protections: - Enable Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG) on Windows. - Use AppArmor or SELinux on Linux for mandatory access controls. Secure Access Settings: - Enable User Account Control (UAC) for Windows. - Restrict root/sudo access on Linux/macOS and enforce strong permissions using sudoers files. File System Hardening: - Implement least-privilege access for critical files and system directories. - Audit permissions regularly using tools like icacls (Windows) or getfacl/chmod (Linux/macOS). Secure Remote Access: - Restrict RDP, SSH, and VNC to authorized IPs using firewall rules. - Enable NLA for RDP and enforce strong password/lockout policies. Harden Boot Configurations: - Enable Secure Boot and enforce UEFI/BIOS password protection. - Use BitLocker or LUKS to encrypt boot drives. Regular Audits: - Periodically audit OS configurations using tools like CIS Benchmarks or SCAP tools. *Tools for Implementation* Windows: - Microsoft Group Policy Objects (GPO): Centrally enforce OS security settings. - Windows Defender Exploit Guard: Built-in OS protection against exploits. - CIS-CAT Pro: Audit Windows security configurations based on CIS Benchmarks. Linux/macOS: - AppArmor/SELinux: Enforce mandatory access controls. - Lynis: Perform comprehensive security audits. - SCAP Security Guide: Automate configuration hardening using Security Content Automation Protocol. Cross-Platform: - Ansible or Chef/Puppet: Automate configuration hardening at scale. - OpenSCAP: Perform compliance and configuration checks.

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
- M1028: https://attack.mitre.org/mitigations/M1028
- Reviewed: 2026-10-27
