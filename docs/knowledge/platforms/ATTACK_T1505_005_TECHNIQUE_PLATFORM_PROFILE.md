# Terminal Services DLL Technique Platform Profile

## Reference

- Technique: **T1505.005 — Terminal Services DLL**
- Platforms named in the source: Windows

Adversaries may abuse components of Terminal Services to enable persistent access to systems. Microsoft Terminal Services, renamed to Remote Desktop Services in some Windows Server OSs as of 2022, enable remote terminal connections to hosts. Terminal Services allows servers to transmit a full, interactive, graphical user interface to clients via RDP. Windows Services that are run as a "generic" process (ex: <code>svchost.exe</code>) load the service's DLL file, the location of which is stored in a Registry entry named <code>ServiceDll</code>. The <code>termsrv.dll</code> file, typically stored in `%SystemRoot%\System32\`, is the default <code>ServiceDll</code> value for Terminal Services in `HKLM\System\CurrentControlSet\services\TermService\Parameters\`. Adversaries may modify and/or replace the Terminal Services DLL to enable persistent access to victimized hosts. Modifications to this DLL could be done to execute arbitrary payloads (while also potentially preserving normal <code>termsrv.dll</code> functionality) as well as to simply enable abusable features of Terminal Services. For example, an adversary may enable features such as concurrent Remote Desktop Protocol sessions by either patching the <code>termsrv.dll</code> file or modifying the <code>ServiceDll</code> value to point to a DLL that provides increased RDP functionality. On a non-server Windows OS this increased functionality may also enable an adversary to avoid Terminal Services prompts that warn/log out users of a system when a new RDP session is created.

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
- T1505.005: https://attack.mitre.org/techniques/T1505/005
- Reviewed: 2026-10-27
