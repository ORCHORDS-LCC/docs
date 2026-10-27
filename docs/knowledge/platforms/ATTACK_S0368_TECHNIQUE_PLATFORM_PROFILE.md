# NotPetya Technique Platform Profile

## Reference

- Technique: **S0368 — NotPetya**
- Platforms named in the source: Windows

NotPetya is malware that was used by Sandworm Team in a worldwide attack starting on June 27, 2017. While NotPetya appears as a form of ransomware, its main purpose was to destroy data and disk structures on compromised systems; the attackers never intended to make the encrypted data recoverable. As such, NotPetya may be more appropriately thought of as a form of wiper malware. NotPetya contains worm-like features to spread itself across a computer network using the SMBv1 exploits EternalBlue and EternalRomance.

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
- S0368: https://attack.mitre.org/software/S0368
- Reviewed: 2026-10-27
