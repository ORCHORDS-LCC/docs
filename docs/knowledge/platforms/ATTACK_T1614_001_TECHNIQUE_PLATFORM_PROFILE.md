# System Language Discovery Technique Platform Profile

## Reference

- Technique: **T1614.001 — System Language Discovery**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities. There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as Query Registry and calls to Native API functions. For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language</code> or parsing the outputs of Windows API functions <code>GetUserDefaultUILanguage</code>, <code>GetSystemDefaultUILanguage</code>, <code>GetKeyboardLayoutList</code> and <code>GetUserDefaultLangID</code>. On a macOS or Linux system, adversaries may query <code>locale</code> to retrieve the value of the <code>$LANG</code> environment variable.

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
- T1614.001: https://attack.mitre.org/techniques/T1614/001
- Reviewed: 2026-10-27
