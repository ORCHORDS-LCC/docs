# Privileged Process Integrity Technique Response Playbook

## Target technique

**M1025 — Privileged Process Integrity**


Privileged Process Integrity focuses on defending highly privileged processes (e.g., system services, antivirus, or authentication processes) from tampering, injection, or compromise by adversaries. These processes often interact with critical components, making them prime targets for techniques like code injection, privilege escalation, and process manipulation. This mitigation can be implemented through the following measures: Protected Process Mechanisms: - Enable RunAsPPL on Windows systems to protect LSASS and other critical processes. - Use registry modifications to enforce protected process settings: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL` Anti-Injection and Memory Protection: - Enable Control Flow Guard (CFG), DEP, and ASLR to protect against process memory tampering. - Deploy endpoint protection tools that actively block process injection attempts. Code Signing Validation: - Implement policies for Windows Defender Application Control (WDAC) or AppLocker to enforce execution of signed binaries. - Ensure critical processes are signed with valid certificates. Access Controls: - Use DACLs and MIC to limit which users and processes can interact with privileged processes. - Disable unnecessary debugging capabilities for high-privileged processes. Kernel-Level Protections: - Ensure Kernel Patch Protection (PatchGuard) is enabled on Windows systems. - Leverage SELinux or AppArmor on Linux to enforce kernel-level security policies. *Tools for Implementation* Protected Process Light (PPL): - RunAsPPL (Windows) - Windows Defender Credential Guard Code Integrity and Signing: - Windows Defender Application Control (WDAC) - AppLocker - SELinux/AppArmor (Linux) Memory Protection: - Control Flow Guard (CFG), Data Execution Prevention (DEP), ASLR Process Isolation/Sandboxing: - Firejail (Linux Sandbox) - Windows Sandbox - QEMU/KVM-based isolation Kernel Protection: - PatchGuard (Windows Kernel Patch Protection) - SELinux (Mandatory Access Control for Linux) - AppArmor.

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
- M1025: https://attack.mitre.org/mitigations/M1025
- Reviewed: 2026-10-27
