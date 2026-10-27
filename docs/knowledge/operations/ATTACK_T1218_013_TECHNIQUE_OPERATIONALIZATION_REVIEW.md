# Mavinject Technique Operationalization Review

## Reference

- Technique: **T1218.013 — Mavinject**

Adversaries may abuse mavinject.exe to proxy execution of malicious code. Mavinject.exe is the Microsoft Application Virtualization Injector, a Windows utility that can inject code into external processes as part of Microsoft Application Virtualization (App-V). Adversaries may abuse mavinject.exe to inject malicious DLLs into running processes (i.e. Dynamic-link Library Injection), allowing for arbitrary code execution (ex. <code>C:\Windows\system32\mavinject.exe PID /INJECTRUNNING PATH_DLL</code>). Since mavinject.exe may be digitally signed by Microsoft, proxying execution via this method may evade detection by security products because the execution is masked under a legitimate process. In addition to Dynamic-link Library Injection, Mavinject.exe can also be abused to perform import descriptor injection via its <code>/HMODULE</code> command-line parameter (ex. <code>mavinject.exe PID /HMODULE=BASE_ADDRESS PATH_DLL ORDINAL_NUMBER</code>). This command would inject an import table entry consisting of the specified DLL into the module at the given base address.

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
- T1218.013: https://attack.mitre.org/techniques/T1218/013
- Reviewed: 2026-10-27
