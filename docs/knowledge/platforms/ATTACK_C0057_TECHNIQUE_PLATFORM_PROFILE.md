# 3CX Supply Chain Attack Technique Platform Profile

## Reference

- Technique: **C0057 — 3CX Supply Chain Attack**
- Platforms named in the source: not stated

The 3CX Supply Chain Attack was the first publicly reported case of one supply chain compromise triggering another, leading to a cascading, two-stage intrusion. The initial supply chain attack began when a 3CX employee downloaded and executed a trojanized, end-of-life version of the X_Trader trading software from Trading Technologies. This provided UNC4736, a threat cluster associated with AppleJeus, access to the 3CX environment. From there UNC4736 compromised the Windows and macOS build environments used to distribute the 3CX desktop application to their customers. While 3CX serves more than 600,000 customers and 12 million users, only a subset of systems were affected. Subsequent targeting focused on victims in the defense and cryptocurrency sectors, where attackers deployed secondary payloads such as Gopuram for credential theft and persistence. The campaign began in late 2022 and was disrupted after security vendors publicly reported the compromise in March 2023.

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
- C0057: https://attack.mitre.org/campaigns/C0057
- Reviewed: 2026-10-27
