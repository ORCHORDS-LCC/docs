# M1044 Restrict Library Loading Outcome Lesson

## Authoritative description

- Technique: **M1044 — Restrict Library Loading**

Restricting library loading involves implementing security controls to ensure that only trusted and verified libraries (DLLs, shared objects, etc.) are loaded into processes. Adversaries often abuse Dynamic-Link Library (DLL) Injection, DLL Search Order Hijacking, or LD_PRELOAD mechanisms to execute malicious code by forcing the operating system to load untrusted libraries. This mitigation can be implemented through the following measures: Enforce Safe Library Loading Practices: - Enable `SafeDLLSearchMode` on Windows. - Restrict `LD_PRELOAD` and `LD_LIBRARY_PATH` usage on Linux systems. Code Signing Enforcement: - Require digital signatures for all libraries loaded into processes. - Use tools like Signtool, and WDAC to enforce signed DLL execution. Environment Hardening: - Secure library paths and directories to prevent adversaries from placing rogue libraries. - Monitor user-writable directories and system configurations for unauthorized changes. Audit and Monitor Library Loading: - Enable `Sysmon` on Windows to monitor for suspicious library loads. - Use `auditd` on Linux to monitor shared library paths and configuration file changes. Use Application Control Solutions: - Implement AppLocker, WDAC, or SELinux to allow only trusted libraries. *Tools for Implementation* Windows-Specific Tools: - AppLocker: Application whitelisting for DLLs. - Windows Defender Application Control (WDAC): Restrict unauthorized library execution. - Signtool: Verify and enforce code signing. - Sysmon: Monitor DLL load events (Event ID 7). Linux-Specific Tools: - auditd: Monitor changes to library paths and critical files. - SELinux/AppArmor: Define policies to restrict library loading. - ldconfig and chattr: Secure LD configuration files and prevent unauthorized modifications. Cross-Platform Solutions: - Wazuh or OSSEC: File integrity monitoring for library changes. - Tripwire: Detect and alert on unauthorized library modifications.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1044: https://attack.mitre.org/mitigations/M1044
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
