# Keylogging Technique Platform Profile

## Reference

- Technique: **T1056.001 — Keylogging**
- Platforms named in the source: Linux, macOS, Network Devices, Windows

Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to be used to acquire credentials for new access opportunities when OS Credential Dumping efforts are not effective, and may require an adversary to intercept keystrokes on a system for a substantial period of time before credentials can be successfully captured. In order to increase the likelihood of capturing credentials quickly, an adversary may also perform actions such as clearing browser cookies to force users to reauthenticate to systems. Keylogging is the most prevalent type of input capture, with many different ways of intercepting keystrokes. Some methods include: * Hooking API callbacks used for processing keystrokes. Unlike Credential API Hooking, this focuses solely on API functions intended for processing keystroke data. * Reading raw keystroke data from the hardware buffer. * Windows Registry modifications. * Custom drivers. * Modify System Image may provide adversaries with hooks into the operating system of network devices to read raw keystrokes for login sessions.

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
- T1056.001: https://attack.mitre.org/techniques/T1056/001
- Reviewed: 2026-10-27
