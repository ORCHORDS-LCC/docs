# RedLine Stealer Technique Platform Profile

## Reference

- Technique: **S1240 — RedLine Stealer**
- Platforms named in the source: Windows

RedLine Stealer is an information-stealer malware variant first identified in 2020. RedLine Stealer is a Malware as a Service (MaaS) and was reportedly sold as either a one-time purchase or a monthly subscription service. Information obtained from RedLine Stealer has been known to be sold on the deep and dark web to Initial Access Brokers (IABs), who use or resell the stolen credentials for further intrusions.

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
- S1240: https://attack.mitre.org/software/S1240
- Reviewed: 2026-10-27
