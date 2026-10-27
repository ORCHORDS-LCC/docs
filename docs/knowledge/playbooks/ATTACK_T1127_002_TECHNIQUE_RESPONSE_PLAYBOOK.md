# ClickOnce Technique Response Playbook

## Target technique

**T1127.002 — ClickOnce**

- Tactics: stealth, execution
- Platforms: Windows

Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code through a trusted Windows utility. ClickOnce is a deployment that enables a user to create self-updating Windows-based .NET applications (i.e, .XBAP, .EXE, or .DLL) that install and run from a file share or web page with minimal user interaction. The application launches as a child process of DFSVC.EXE, which is responsible for installing, launching, and updating the application. Because ClickOnce applications receive only limited permissions, they do not require administrative permissions to install. As such, adversaries may abuse ClickOnce to proxy execution of malicious code without needing to escalate privileges. ClickOnce may be abused in a number of ways. For example, an adversary may rely on User Execution. When a user visits a malicious website, the .NET malware is disguised as legitimate software and a ClickOnce popup is displayed for installation. Adversaries may also abuse ClickOnce to execute malware via a Rundll32 script using the command `rundll32.exe dfshim.dll,ShOpenVerbApplication1`. Additionally, an adversary can move the ClickOnce application file to a remote user’s startup folder for continued malicious code deployment (i.e., Registry Run Keys / Startup Folder).

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1127.002: https://attack.mitre.org/techniques/T1127/002
- Reviewed: 2026-10-27
