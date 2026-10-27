# ArcaneDoor Technique Platform Profile

## Reference

- Technique: **C0046 — ArcaneDoor**
- Platforms named in the source: not stated

ArcaneDoor is a campaign targeting networking devices from Cisco and other vendors between July 2023 and April 2024, primarily focused on government and critical infrastructure networks. ArcaneDoor is associated with the deployment of the custom backdoors Line Runner and Line Dancer. ArcaneDoor is attributed to a group referred to as UAT4356 or STORM-1849, and is assessed to be a state-sponsored campaign.

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
- C0046: https://attack.mitre.org/campaigns/C0046
- Reviewed: 2026-10-27
