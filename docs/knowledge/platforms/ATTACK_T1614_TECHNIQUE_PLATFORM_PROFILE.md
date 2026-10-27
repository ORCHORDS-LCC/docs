# System Location Discovery Technique Platform Profile

## Reference

- Technique: **T1614 — System Location Discovery**
- Platforms named in the source: IaaS, Linux, macOS, Windows

Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from System Location Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings. Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of the host. In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance. Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.

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
- T1614: https://attack.mitre.org/techniques/T1614
- Reviewed: 2026-10-27
