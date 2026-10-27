# Volt Typhoon Technique Platform Profile

## Reference

- Technique: **G1017 — Volt Typhoon**
- Platforms named in the source: not stated

Volt Typhoon is a People's Republic of China (PRC) state-sponsored actor that has been active since at least 2021, primarily targeting critical infrastructure organizations in the US and its territories including Guam. Volt Typhoon's targeting and pattern of behavior have been assessed as pre-positioning to enable lateral movement to operational technology (OT) assets for potential destructive or disruptive attacks. Volt Typhoon has emphasized stealth in operations using web shells, living-off-the-land (LOTL) binaries, hands on keyboard activities, and stolen credentials.. The group has leveraged compromised SOHO routers to proxy command and control traffic and obscure its infrastructure, activity associated with the KV botnet.. Reporting indicates a separate initial access cluster, SYLVANITE, has been observed exploiting internet-facing edge devices and transferring access to Volt Typhoon, also tracked as VOLTZITE, for follow-on operations.

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
- G1017: https://attack.mitre.org/groups/G1017
- Reviewed: 2026-10-27
