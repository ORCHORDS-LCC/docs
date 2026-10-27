# AcidPour Technique Platform Profile

## Reference

- Technique: **S1167 — AcidPour**
- Platforms named in the source: Linux

AcidPour is a variant of AcidRain designed to impact a wider range of x86 architecture Linux devices. AcidPour is an x86 ELF binary that expands on the targeted devices and locations in AcidRain by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, AcidPour can impact a variety of device types including IoT, networking, and ICS embedded device types. AcidPour is a wiping payload associated with the Sandworm Team threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.

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
- S1167: https://attack.mitre.org/software/S1167
- Reviewed: 2026-10-27
