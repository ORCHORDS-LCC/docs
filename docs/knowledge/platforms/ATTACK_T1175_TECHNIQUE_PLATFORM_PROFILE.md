# Distributed Component Object Model Mitigation Technique Platform Profile

## Reference

- Technique: **T1175 — Distributed Component Object Model Mitigation**
- Platforms named in the source: not stated

Modify Registry settings (directly or using Dcomcnfg.exe) in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\{AppID_GUID}</code> associated with the process-wide security of individual COM applications. Modify Registry settings (directly or using Dcomcnfg.exe) in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole</code> associated with system-wide security defaults for all COM applications that do no set their own process-wide security. Consider disabling DCOM through Dcomcnfg.exe. Enable Windows firewall, which prevents DCOM instantiation by default. Ensure all COM alerts and Protected View are enabled.

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
- T1175: https://attack.mitre.org/mitigations/T1175
- Reviewed: 2026-10-27
