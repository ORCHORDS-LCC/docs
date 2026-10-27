# Shamoon Technique Platform Profile

## Reference

- Technique: **S0140 — Shamoon**
- Platforms named in the source: Windows

Shamoon is wiper malware that was first used by an Iranian group known as the "Cutting Sword of Justice" in 2012. Other versions known as Shamoon 2 and Shamoon 3 were observed in 2016 and 2018. Shamoon has also been seen leveraging RawDisk and Filerase to carry out data wiping tasks. Analysis has linked Shamoon with Kwampirs based on multiple shared artifacts and coding patterns. The term Shamoon is sometimes used to refer to the group using the malware as well as the malware itself.

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
- S0140: https://attack.mitre.org/software/S0140
- Reviewed: 2026-10-27
