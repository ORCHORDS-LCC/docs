# Leviathan Australian Intrusions Technique Platform Profile

## Reference

- Technique: **C0049 — Leviathan Australian Intrusions**
- Platforms named in the source: not stated

Leviathan Australian Intrusions consisted of at least two long-term intrusions against victims in Australia by Leviathan, relying on similar tradecraft such as external service exploitation followed by extensive credential capture and re-use to enable privilege escalation and lateral movement. Leviathan Australian Intrusions were focused on exfiltrating sensitive data including valid credentials for the victim organizations.

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
- C0049: https://attack.mitre.org/campaigns/C0049
- Reviewed: 2026-10-27
