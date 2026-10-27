# SyncAppvPublishingServer Technique Platform Profile

## Reference

- Technique: **T1216.002 — SyncAppvPublishingServer**
- Platforms named in the source: Windows

Adversaries may abuse SyncAppvPublishingServer.vbs to proxy execution of malicious PowerShell commands. SyncAppvPublishingServer.vbs is a Visual Basic script associated with how Windows virtualizes applications (Microsoft Application Virtualization, or App-V). For example, Windows may render Win32 applications to users as virtual applications, allowing users to launch and interact with them as if they were installed locally. The SyncAppvPublishingServer.vbs script is legitimate, may be signed by Microsoft, and is commonly executed from `\System32` through the command line via `wscript.exe`. Adversaries may abuse SyncAppvPublishingServer.vbs to bypass PowerShell execution restrictions and evade defensive counter measures by "living off the land." Proxying execution may function as a trusted/signed alternative to directly invoking `powershell.exe`. For example, PowerShell commands may be invoked using: `SyncAppvPublishingServer.vbs "n; {PowerShell}"`.

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
- T1216.002: https://attack.mitre.org/techniques/T1216/002
- Reviewed: 2026-10-27
