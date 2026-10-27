# STATICPLUGIN Technique Platform Profile

## Reference

- Technique: **S1238 — STATICPLUGIN**
- Platforms named in the source: Windows

STATICPLUGIN is a downloader known to be leveraged by Mustang Panda and was first observed utilized in 2025. STATICPLUGIN has utilized a valid certificate in order to bypass endpoint security protections. STATICPLUGIN masqueraded as legitimate software installer by using a custom TForm. STATICPLUGIN has been leveraged to deploy a loader that facilitates follow on malware.

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
- S1238: https://attack.mitre.org/software/S1238
- Reviewed: 2026-10-27
