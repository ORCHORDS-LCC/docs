# APT42 Technique Platform Profile

## Reference

- Technique: **G1044 — APT42**
- Platforms named in the source: not stated

APT42 is an Iranian-sponsored threat group that conducts cyber espionage and surveillance. The group primarily focuses on targets in the Middle East region, but has targeted a variety of industries and countries since at least 2015. APT42 starts cyber operations through spearphishing emails and/or the PINEFLOWER Android malware, then monitors and collects information from the compromised systems and devices. Finally, APT42 exfiltrates data using native features and open-source tools. APT42 activities have been linked to Magic Hound by other commercial vendors. While there are behavior and software overlaps between Magic Hound and APT42, they appear to be distinct entities and are tracked as separate entities by their originating vendor.

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
- G1044: https://attack.mitre.org/groups/G1044
- Reviewed: 2026-10-27
