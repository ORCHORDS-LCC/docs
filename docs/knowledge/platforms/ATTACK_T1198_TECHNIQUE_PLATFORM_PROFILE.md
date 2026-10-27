# SIP and Trust Provider Hijacking Mitigation Technique Platform Profile

## Reference

- Technique: **T1198 — SIP and Trust Provider Hijacking Mitigation**
- Platforms named in the source: not stated

Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Also ensure that these values contain their full path to prevent DLL Search Order Hijacking. Consider removing unnecessary and/or stale SIPs. Restrict storage and execution of SIP DLLs to protected directories, such as C:\Windows, rather than user directories. Enable whitelisting solutions such as AppLocker and/or Device Guard to block the loading of malicious SIP DLLs. Components may still be able to be hijacked to suitable functions already present on disk if malicious modifications to Registry keys are not prevented.

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
- T1198: https://attack.mitre.org/mitigations/T1198
- Reviewed: 2026-10-27
