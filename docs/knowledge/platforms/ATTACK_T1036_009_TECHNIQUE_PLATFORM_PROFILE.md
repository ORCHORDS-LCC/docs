# Break Process Trees Technique Platform Profile

## Reference

- Technique: **T1036.009 — Break Process Trees**
- Platforms named in the source: Linux, macOS

An adversary may attempt to evade process tree-based analysis by modifying executed malware's parent process ID (PPID). If endpoint protection software leverages the “parent-child" relationship for detection, breaking this relationship could result in the adversary’s behavior not being associated with previous process tree activity. On Unix-based systems breaking this process tree is common practice for administrators to execute software using scripts and programs. On Linux systems, adversaries may execute a series of Native API calls to alter malware's process tree. For example, adversaries can execute their payload without any arguments, call the `fork()` API call twice, then have the parent process exit. This creates a grandchild process with no parent process that is immediately adopted by the `init` system process (PID 1), which successfully disconnects the execution of the adversary's payload from its previous process tree. Another example is using the “daemon” syscall to detach from the current parent process and run in the background.

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
- T1036.009: https://attack.mitre.org/techniques/T1036/009
- Reviewed: 2026-10-27
