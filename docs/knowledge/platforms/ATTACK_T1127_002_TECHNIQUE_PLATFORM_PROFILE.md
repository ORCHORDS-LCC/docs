# ClickOnce Technique Platform Profile

## Reference

- Technique: **T1127.002 — ClickOnce**
- Platforms named in the source: Windows

Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code through a trusted Windows utility. ClickOnce is a deployment that enables a user to create self-updating Windows-based .NET applications (i.e, .XBAP, .EXE, or .DLL) that install and run from a file share or web page with minimal user interaction. The application launches as a child process of DFSVC.EXE, which is responsible for installing, launching, and updating the application. Because ClickOnce applications receive only limited permissions, they do not require administrative permissions to install. As such, adversaries may abuse ClickOnce to proxy execution of malicious code without needing to escalate privileges. ClickOnce may be abused in a number of ways. For example, an adversary may rely on User Execution. When a user visits a malicious website, the .NET malware is disguised as legitimate software and a ClickOnce popup is displayed for installation. Adversaries may also abuse ClickOnce to execute malware via a Rundll32 script using the command `rundll32.exe dfshim.dll,ShOpenVerbApplication1`. Additionally, an adversary can move the ClickOnce application file to a remote user’s startup folder for continued malicious code deployment (i.e., Registry Run Keys / Startup Folder).

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
- T1127.002: https://attack.mitre.org/techniques/T1127/002
- Reviewed: 2026-10-27
