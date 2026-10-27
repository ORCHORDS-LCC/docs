# System Owner/User Discovery Technique Platform Profile

## Reference

- Technique: **T1033 — System Owner/User Discovery**
- Platforms named in the source: Linux, macOS, Network Devices, Windows

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using OS Credential Dumping. The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from System Owner/User Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. Various utilities and commands may acquire this information, including whoami. In macOS and Linux, the currently logged in user can be identified with w and who. On macOS the dscl . list /Users | grep -v '_' command can also be used to enumerate user accounts. Environment variables, such as %USERNAME% and $USER, may also be used to access this information. On network devices, Network Device CLI commands such as `show users` and `show ssh` can be used to display users currently logged into the device.

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
- T1033: https://attack.mitre.org/techniques/T1033
- Reviewed: 2026-10-27
