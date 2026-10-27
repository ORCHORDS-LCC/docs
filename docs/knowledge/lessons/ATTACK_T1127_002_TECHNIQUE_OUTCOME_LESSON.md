# T1127.002 ClickOnce Outcome Lesson

## Authoritative description

- Technique: **T1127.002 — ClickOnce**
- Tactics: stealth, execution
- Platforms: Windows

Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code through a trusted Windows utility. ClickOnce is a deployment that enables a user to create self-updating Windows-based .NET applications (i.e, .XBAP, .EXE, or .DLL) that install and run from a file share or web page with minimal user interaction. The application launches as a child process of DFSVC.EXE, which is responsible for installing, launching, and updating the application. Because ClickOnce applications receive only limited permissions, they do not require administrative permissions to install. As such, adversaries may abuse ClickOnce to proxy execution of malicious code without needing to escalate privileges. ClickOnce may be abused in a number of ways. For example, an adversary may rely on User Execution. When a user visits a malicious website, the .NET malware is disguised as legitimate software and a ClickOnce popup is displayed for installation. Adversaries may also abuse ClickOnce to execute malware via a Rundll32 script using the command `rundll32.exe dfshim.dll,ShOpenVerbApplication1`. Additionally, an adversary can move the ClickOnce application file to a remote user’s startup folder for continued malicious code deployment (i.e., Registry Run Keys / Startup Folder).

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
- T1127.002: https://attack.mitre.org/techniques/T1127/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
