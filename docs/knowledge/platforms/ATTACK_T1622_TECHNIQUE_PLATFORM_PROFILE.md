# Debugger Evasion Technique Platform Profile

## Reference

- Technique: **T1622 — Debugger Evasion**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads. Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to Virtualization/Sandbox Evasion, if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads. Specific checks will vary based on the target and/or adversary. On Windows, this may involve Native API function calls such as <code>IsDebuggerPresent()</code> and <code> NtQueryInformationProcess()</code>, or manually checking the <code>BeingDebugged</code> flag of the Process Environment Block (PEB). On Linux, this may involve querying `/proc/self/status` for the `TracerPID` field, which indicates whether or not the process is being traced by dynamic analysis tools. Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would “swallow” or handle the potential error). Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler, which will automatically handle the exception and allow the program’s execution to continue. Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping Native API function calls such as <code>OutputDebugStringW()</code>.

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
- T1622: https://attack.mitre.org/techniques/T1622
- Reviewed: 2026-10-27
