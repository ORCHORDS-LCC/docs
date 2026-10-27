# Inter-Process Communication Technique Platform Profile

## Reference

- Technique: **T1559 — Inter-Process Communication**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows Dynamic Data Exchange or Component Object Model. Linux environments support several different IPC mechanisms, two of which being sockets and pipes. Higher level execution mediums, such as those of Command and Scripting Interpreters, may also leverage underlying IPC mechanisms. Adversaries may also use Remote Services such as Distributed Component Object Model to facilitate remote IPC execution.

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
- T1559: https://attack.mitre.org/techniques/T1559
- Reviewed: 2026-10-27
