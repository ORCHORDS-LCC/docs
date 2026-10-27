# Restrict Library Loading Technique Platform Profile

## Reference

- Technique: **M1044 — Restrict Library Loading**
- Platforms named in the source: not stated

Restricting library loading involves implementing security controls to ensure that only trusted and verified libraries (DLLs, shared objects, etc.) are loaded into processes. Adversaries often abuse Dynamic-Link Library (DLL) Injection, DLL Search Order Hijacking, or LD_PRELOAD mechanisms to execute malicious code by forcing the operating system to load untrusted libraries. This mitigation can be implemented through the following measures: Enforce Safe Library Loading Practices: - Enable `SafeDLLSearchMode` on Windows. - Restrict `LD_PRELOAD` and `LD_LIBRARY_PATH` usage on Linux systems. Code Signing Enforcement: - Require digital signatures for all libraries loaded into processes. - Use tools like Signtool, and WDAC to enforce signed DLL execution. Environment Hardening: - Secure library paths and directories to prevent adversaries from placing rogue libraries. - Monitor user-writable directories and system configurations for unauthorized changes. Audit and Monitor Library Loading: - Enable `Sysmon` on Windows to monitor for suspicious library loads. - Use `auditd` on Linux to monitor shared library paths and configuration file changes. Use Application Control Solutions: - Implement AppLocker, WDAC, or SELinux to allow only trusted libraries. *Tools for Implementation* Windows-Specific Tools: - AppLocker: Application whitelisting for DLLs. - Windows Defender Application Control (WDAC): Restrict unauthorized library execution. - Signtool: Verify and enforce code signing. - Sysmon: Monitor DLL load events (Event ID 7). Linux-Specific Tools: - auditd: Monitor changes to library paths and critical files. - SELinux/AppArmor: Define policies to restrict library loading. - ldconfig and chattr: Secure LD configuration files and prevent unauthorized modifications. Cross-Platform Solutions: - Wazuh or OSSEC: File integrity monitoring for library changes. - Tripwire: Detect and alert on unauthorized library modifications.

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
- M1044: https://attack.mitre.org/mitigations/M1044
- Reviewed: 2026-10-27
