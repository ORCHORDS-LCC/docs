# SyncAppvPublishingServer Technique Response Playbook

## Target technique

**T1216.002 — SyncAppvPublishingServer**

- Tactics: stealth
- Platforms: Windows

Adversaries may abuse SyncAppvPublishingServer.vbs to proxy execution of malicious PowerShell commands. SyncAppvPublishingServer.vbs is a Visual Basic script associated with how Windows virtualizes applications (Microsoft Application Virtualization, or App-V). For example, Windows may render Win32 applications to users as virtual applications, allowing users to launch and interact with them as if they were installed locally. The SyncAppvPublishingServer.vbs script is legitimate, may be signed by Microsoft, and is commonly executed from `\System32` through the command line via `wscript.exe`. Adversaries may abuse SyncAppvPublishingServer.vbs to bypass PowerShell execution restrictions and evade defensive counter measures by "living off the land." Proxying execution may function as a trusted/signed alternative to directly invoking `powershell.exe`. For example, PowerShell commands may be invoked using: `SyncAppvPublishingServer.vbs "n; {PowerShell}"`.

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
- T1216.002: https://attack.mitre.org/techniques/T1216/002
- Reviewed: 2026-10-27
