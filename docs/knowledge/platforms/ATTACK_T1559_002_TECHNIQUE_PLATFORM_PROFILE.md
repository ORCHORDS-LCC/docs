# Dynamic Data Exchange Technique Platform Profile

## Reference

- Technique: **T1559.002 — Dynamic Data Exchange**
- Platforms named in the source: Windows

Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution. Object Linking and Embedding (OLE), or the ability to link data between documents, was originally implemented through DDE. Despite being superseded by Component Object Model, DDE may be enabled in Windows 10 and most of Microsoft Office 2016 via Registry keys. Microsoft Office documents can be poisoned with DDE commands, directly or through embedded files, and used to deliver execution via Phishing campaigns or hosted Web content, avoiding the use of Visual Basic for Applications (VBA) macros. Similarly, adversaries may infect payloads to execute applications and/or commands on a victim device by way of embedding DDE formulas within a CSV file intended to be opened through a Windows spreadsheet program. DDE could also be leveraged by an adversary operating on a compromised machine who does not have direct access to a Command and Scripting Interpreter. DDE execution can be invoked remotely via Remote Services such as Distributed Component Object Model (DCOM).

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
- T1559.002: https://attack.mitre.org/techniques/T1559/002
- Reviewed: 2026-10-27
