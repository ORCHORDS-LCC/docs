# Restrict Library Loading Technique Engineering Review

## Reference

- Technique: **M1044 — Restrict Library Loading**

Restricting library loading involves implementing security controls to ensure that only trusted and verified libraries (DLLs, shared objects, etc.) are loaded into processes. Adversaries often abuse Dynamic-Link Library (DLL) Injection, DLL Search Order Hijacking, or LD_PRELOAD mechanisms to execute malicious code by forcing the operating system to load untrusted libraries. This mitigation can be implemented through the following measures: Enforce Safe Library Loading Practices: - Enable `SafeDLLSearchMode` on Windows. - Restrict `LD_PRELOAD` and `LD_LIBRARY_PATH` usage on Linux systems. Code Signing Enforcement: - Require digital signatures for all libraries loaded into processes. - Use tools like Signtool, and WDAC to enforce signed DLL execution. Environment Hardening: - Secure library paths and directories to prevent adversaries from placing rogue libraries. - Monitor user-writable directories and system configurations for unauthorized changes. Audit and Monitor Library Loading: - Enable `Sysmon` on Windows to monitor for suspicious library loads. - Use `auditd` on Linux to monitor shared library paths and configuration file changes. Use Application Control Solutions: - Implement AppLocker, WDAC, or SELinux to allow only trusted libraries. *Tools for Implementation* Windows-Specific Tools: - AppLocker: Application whitelisting for DLLs. - Windows Defender Application Control (WDAC): Restrict unauthorized library execution. - Signtool: Verify and enforce code signing. - Sysmon: Monitor DLL load events (Event ID 7). Linux-Specific Tools: - auditd: Monitor changes to library paths and critical files. - SELinux/AppArmor: Define policies to restrict library loading. - ldconfig and chattr: Secure LD configuration files and prevent unauthorized modifications. Cross-Platform Solutions: - Wazuh or OSSEC: File integrity monitoring for library changes. - Tripwire: Detect and alert on unauthorized library modifications.

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
- M1044: https://attack.mitre.org/mitigations/M1044
- Reviewed: 2026-10-27
