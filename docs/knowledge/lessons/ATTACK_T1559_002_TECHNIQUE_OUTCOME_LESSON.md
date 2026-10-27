# T1559.002 Dynamic Data Exchange Outcome Lesson

## Authoritative description

- Technique: **T1559.002 — Dynamic Data Exchange**
- Tactics: execution
- Platforms: Windows

Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution. Object Linking and Embedding (OLE), or the ability to link data between documents, was originally implemented through DDE. Despite being superseded by Component Object Model, DDE may be enabled in Windows 10 and most of Microsoft Office 2016 via Registry keys. Microsoft Office documents can be poisoned with DDE commands, directly or through embedded files, and used to deliver execution via Phishing campaigns or hosted Web content, avoiding the use of Visual Basic for Applications (VBA) macros. Similarly, adversaries may infect payloads to execute applications and/or commands on a victim device by way of embedding DDE formulas within a CSV file intended to be opened through a Windows spreadsheet program. DDE could also be leveraged by an adversary operating on a compromised machine who does not have direct access to a Command and Scripting Interpreter. DDE execution can be invoked remotely via Remote Services such as Distributed Component Object Model (DCOM).

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1559.002: https://attack.mitre.org/techniques/T1559/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
