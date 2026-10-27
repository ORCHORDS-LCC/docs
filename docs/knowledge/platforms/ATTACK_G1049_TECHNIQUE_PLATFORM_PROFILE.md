# AppleJeus Technique Platform Profile

## Reference

- Technique: **G1049 — AppleJeus**
- Platforms named in the source: not stated

AppleJeus is a North Korean state-sponsored threat group attributed to the Reconnaissance General Bureau. Associated with the broader Lazarus Group umbrella of actors, AppleJeus has been active since at least 2018 and is closely aligned in resources with TEMP.hermit, another DPRK-affiliated group under the same umbrella. The group’s primary mission is to generate and launder revenue to provide financial support to the government. AppleJeus primarily targets the cryptocurrency industry and is most notably responsible for the 3CX Supply Chain Attack. The group traditionally deploys malicious cryptocurrency software in combination with Phishing. From these compromised environments, it selectively deploys additional backdoors to enable extended operations against high-value financial targets.

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
- G1049: https://attack.mitre.org/groups/G1049
- Reviewed: 2026-10-27
