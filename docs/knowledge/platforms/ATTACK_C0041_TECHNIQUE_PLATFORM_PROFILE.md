# FrostyGoop Incident Technique Platform Profile

## Reference

- Technique: **C0041 — FrostyGoop Incident**
- Platforms named in the source: not stated

FrostyGoop Incident took place in January 2024 against a municipal district heating company in Ukraine. Following initial access via likely exploitation of external facing services, FrostyGoop was used to manipulate ENCO control systems via legitimate Modbus commands to impact the delivery of heating services to Ukrainian civilians.

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
- C0041: https://attack.mitre.org/campaigns/C0041
- Reviewed: 2026-10-27
