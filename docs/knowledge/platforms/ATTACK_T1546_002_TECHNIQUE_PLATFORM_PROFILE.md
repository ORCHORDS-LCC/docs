# Screensaver Technique Platform Profile

## Reference

- Technique: **T1546.002 — Screensaver**
- Platforms named in the source: Windows

Adversaries may establish persistence by executing malicious content triggered by user inactivity. Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension. The Windows screensaver application scrnsave.scr is located in <code>C:\Windows\System32\</code>, and <code>C:\Windows\sysWOW64\</code> on 64-bit Windows systems, along with screensavers included with base Windows installations. The following screensaver settings are stored in the Registry (<code>HKCU\Control Panel\Desktop\</code>) and could be manipulated to achieve persistence: * <code>SCRNSAVE.exe</code> - set to malicious PE path * <code>ScreenSaveActive</code> - set to '1' to enable the screensaver * <code>ScreenSaverIsSecure</code> - set to '0' to not require a password to unlock * <code>ScreenSaveTimeout</code> - sets user inactivity timeout before screensaver is executed Adversaries can use screensaver settings to maintain persistence by setting the screensaver to run malware after a certain timeframe of user inactivity.

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
- T1546.002: https://attack.mitre.org/techniques/T1546/002
- Reviewed: 2026-10-27
