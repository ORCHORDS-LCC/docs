# File System Permissions Weakness Mitigation Technique Engineering Review

## Reference

- Technique: **T1044 — File System Permissions Weakness Mitigation**

Use auditing tools capable of detecting file system permissions abuse opportunities on systems within an enterprise and correct them. Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service binary target path locations. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for service file system permissions weaknesses. Identify and block potentially malicious software that may be executed through abuse of file, directory, and service permissions by using whitelisting tools, like AppLocker, that are capable of auditing and/or blocking unknown programs. Deny execution from user directories such as file download directories and temp directories where able. Turn off UAC's privilege elevation for standard users [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]to automatically deny elevation requests, add: "ConsentPromptBehaviorUser"=dword:00000000 . Consider enabling installer detection for all users by adding: "EnableInstallerDetection"=dword:00000001. This will prompt for a password for installation and also log the attempt. To disable installer detection, instead add: "EnableInstallerDetection"=dword:00000000. This may prevent potential elevation of privileges through exploitation during the process of UAC detecting the installer, but will allow the installation process to continue without being logged.

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
- T1044: https://attack.mitre.org/mitigations/T1044
- Reviewed: 2026-10-27
