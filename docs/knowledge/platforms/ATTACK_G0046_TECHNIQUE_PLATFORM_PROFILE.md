# FIN7 Technique Platform Profile

## Reference

- Technique: **G0046 — FIN7**
- Platforms named in the source: not stated

FIN7 is a financially-motivated threat group that has been active since 2013. FIN7 has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. A portion of FIN7 was operated out of a front company called Combi Security and often used point-of-sale malware for targeting efforts. Since 2020, FIN7 shifted operations to big game hunting (BGH), including use of REvil ransomware and their own Ransomware-as-a-Service (RaaS), Darkside. FIN7 may be linked to the Carbanak Group, but multiple threat groups have been observed using Carbanak, leading these groups to be tracked separately.

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
- G0046: https://attack.mitre.org/groups/G0046
- Reviewed: 2026-10-27
