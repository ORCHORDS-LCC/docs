# KV Botnet Activity Technique Platform Profile

## Reference

- Technique: **C0035 — KV Botnet Activity**
- Platforms named in the source: not stated

KV Botnet Activity consisted of exploitation of primarily “end-of-life” small office-home office (SOHO) equipment from manufacturers such as Cisco, NETGEAR, and DrayTek. KV Botnet Activity was used by Volt Typhoon to obfuscate connectivity to victims in multiple critical infrastructure segments, including energy and telecommunication companies and entities based on the US territory of Guam. While the KV Botnet is the most prominent element of this campaign, it overlaps with another botnet cluster referred to as the JDY cluster. This botnet was disrupted by US law enforcement entities in early 2024 after periods of activity from October 2022 through January 2024.

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
- C0035: https://attack.mitre.org/campaigns/C0035
- Reviewed: 2026-10-27
