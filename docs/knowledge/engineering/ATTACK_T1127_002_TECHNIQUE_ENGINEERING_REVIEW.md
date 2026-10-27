# ClickOnce Technique Engineering Review

## Reference

- Technique: **T1127.002 — ClickOnce**

Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code through a trusted Windows utility. ClickOnce is a deployment that enables a user to create self-updating Windows-based .NET applications (i.e, .XBAP, .EXE, or .DLL) that install and run from a file share or web page with minimal user interaction. The application launches as a child process of DFSVC.EXE, which is responsible for installing, launching, and updating the application. Because ClickOnce applications receive only limited permissions, they do not require administrative permissions to install. As such, adversaries may abuse ClickOnce to proxy execution of malicious code without needing to escalate privileges. ClickOnce may be abused in a number of ways. For example, an adversary may rely on User Execution. When a user visits a malicious website, the .NET malware is disguised as legitimate software and a ClickOnce popup is displayed for installation. Adversaries may also abuse ClickOnce to execute malware via a Rundll32 script using the command `rundll32.exe dfshim.dll,ShOpenVerbApplication1`. Additionally, an adversary can move the ClickOnce application file to a remote user’s startup folder for continued malicious code deployment (i.e., Registry Run Keys / Startup Folder).

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1127.002: https://attack.mitre.org/techniques/T1127/002
- Reviewed: 2026-10-27
