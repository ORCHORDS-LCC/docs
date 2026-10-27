# ClickOnce Technique Operationalization Review

## Reference

- Technique: **T1127.002 — ClickOnce**

Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code through a trusted Windows utility. ClickOnce is a deployment that enables a user to create self-updating Windows-based .NET applications (i.e, .XBAP, .EXE, or .DLL) that install and run from a file share or web page with minimal user interaction. The application launches as a child process of DFSVC.EXE, which is responsible for installing, launching, and updating the application. Because ClickOnce applications receive only limited permissions, they do not require administrative permissions to install. As such, adversaries may abuse ClickOnce to proxy execution of malicious code without needing to escalate privileges. ClickOnce may be abused in a number of ways. For example, an adversary may rely on User Execution. When a user visits a malicious website, the .NET malware is disguised as legitimate software and a ClickOnce popup is displayed for installation. Adversaries may also abuse ClickOnce to execute malware via a Rundll32 script using the command `rundll32.exe dfshim.dll,ShOpenVerbApplication1`. Additionally, an adversary can move the ClickOnce application file to a remote user’s startup folder for continued malicious code deployment (i.e., Registry Run Keys / Startup Folder).

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1127.002: https://attack.mitre.org/techniques/T1127/002
- Reviewed: 2026-10-27
