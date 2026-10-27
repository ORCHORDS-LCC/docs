# Graphical User Interface Technique Platform Profile

## Reference

- Technique: **T1061 — Graphical User Interface**
- Platforms named in the source: Linux, macOS, Windows

**This technique has been deprecated. Please use Remote Services where appropriate.** The Graphical User Interfaces (GUI) is a common way to interact with an operating system. Adversaries may use a system's GUI during an operation, commonly through a remote interactive session such as Remote Desktop Protocol, instead of through a Command and Scripting Interpreter, to search for information and execute files via mouse double-click events, the Windows Run command , or other potentially difficult to monitor interactions.

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
- T1061: https://attack.mitre.org/techniques/T1061
- Reviewed: 2026-10-27
