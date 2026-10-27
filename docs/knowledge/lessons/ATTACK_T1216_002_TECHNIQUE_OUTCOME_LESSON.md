# T1216.002 SyncAppvPublishingServer Outcome Lesson

## Authoritative description

- Technique: **T1216.002 — SyncAppvPublishingServer**
- Tactics: stealth
- Platforms: Windows

Adversaries may abuse SyncAppvPublishingServer.vbs to proxy execution of malicious PowerShell commands. SyncAppvPublishingServer.vbs is a Visual Basic script associated with how Windows virtualizes applications (Microsoft Application Virtualization, or App-V). For example, Windows may render Win32 applications to users as virtual applications, allowing users to launch and interact with them as if they were installed locally. The SyncAppvPublishingServer.vbs script is legitimate, may be signed by Microsoft, and is commonly executed from `\System32` through the command line via `wscript.exe`. Adversaries may abuse SyncAppvPublishingServer.vbs to bypass PowerShell execution restrictions and evade defensive counter measures by "living off the land." Proxying execution may function as a trusted/signed alternative to directly invoking `powershell.exe`. For example, PowerShell commands may be invoked using: `SyncAppvPublishingServer.vbs "n; {PowerShell}"`.

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
- T1216.002: https://attack.mitre.org/techniques/T1216/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
