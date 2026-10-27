# Mavinject Technique Platform Profile

## Reference

- Technique: **T1218.013 — Mavinject**
- Platforms named in the source: Windows

Adversaries may abuse mavinject.exe to proxy execution of malicious code. Mavinject.exe is the Microsoft Application Virtualization Injector, a Windows utility that can inject code into external processes as part of Microsoft Application Virtualization (App-V). Adversaries may abuse mavinject.exe to inject malicious DLLs into running processes (i.e. Dynamic-link Library Injection), allowing for arbitrary code execution (ex. <code>C:\Windows\system32\mavinject.exe PID /INJECTRUNNING PATH_DLL</code>). Since mavinject.exe may be digitally signed by Microsoft, proxying execution via this method may evade detection by security products because the execution is masked under a legitimate process. In addition to Dynamic-link Library Injection, Mavinject.exe can also be abused to perform import descriptor injection via its <code>/HMODULE</code> command-line parameter (ex. <code>mavinject.exe PID /HMODULE=BASE_ADDRESS PATH_DLL ORDINAL_NUMBER</code>). This command would inject an import table entry consisting of the specified DLL into the module at the given base address.

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
- T1218.013: https://attack.mitre.org/techniques/T1218/013
- Reviewed: 2026-10-27
