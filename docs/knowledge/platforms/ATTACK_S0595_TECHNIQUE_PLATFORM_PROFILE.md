# ThiefQuest Technique Platform Profile

## Reference

- Technique: **S0595 — ThiefQuest**
- Platforms named in the source: macOS

ThiefQuest is a virus, data stealer, and wiper that presents itself as ransomware targeting macOS systems. ThiefQuest was first seen in 2020 distributed via trojanized pirated versions of popular macOS software on Russian forums sharing torrent links. Even though ThiefQuest presents itself as ransomware, since the dynamically generated encryption key is never sent to the attacker it may be more appropriately thought of as a form of wiper malware.

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
- S0595: https://attack.mitre.org/software/S0595
- Reviewed: 2026-10-27
