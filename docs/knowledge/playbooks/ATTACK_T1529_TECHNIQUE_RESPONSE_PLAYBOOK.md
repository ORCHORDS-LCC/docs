# System Shutdown/Reboot Technique Response Playbook

## Target technique

**T1529 — System Shutdown/Reboot**

- Tactics: impact
- Platforms: ESXi, Linux, macOS, Network Devices, Windows

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via Network Device CLI (e.g. <code>reload</code>). They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools. Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery. Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot. Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system. In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via Access Token Manipulation). In some cases, the system may not be able to boot again. Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as Disk Structure Wipe or Inhibit System Recovery, to hasten the intended effects on system availability.

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
- T1529: https://attack.mitre.org/techniques/T1529
- Reviewed: 2026-10-27
