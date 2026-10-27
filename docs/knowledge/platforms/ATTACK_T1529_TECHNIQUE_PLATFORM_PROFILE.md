# System Shutdown/Reboot Technique Platform Profile

## Reference

- Technique: **T1529 — System Shutdown/Reboot**
- Platforms named in the source: ESXi, Linux, macOS, Network Devices, Windows

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via Network Device CLI (e.g. <code>reload</code>). They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools. Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery. Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot. Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system. In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via Access Token Manipulation). In some cases, the system may not be able to boot again. Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as Disk Structure Wipe or Inhibit System Recovery, to hasten the intended effects on system availability.

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
- T1529: https://attack.mitre.org/techniques/T1529
- Reviewed: 2026-10-27
