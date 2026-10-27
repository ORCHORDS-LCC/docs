# AcidRain Technique Platform Profile

## Reference

- Technique: **S1125 — AcidRain**
- Platforms named in the source: Network Devices, Linux

AcidRain is an ELF binary targeting modems and routers using MIPS architecture. AcidRain is associated with the ViaSat KA-SAT communication outage that took place during the initial phases of the 2022 full-scale invasion of Ukraine. Analysis indicates overlap with another network device-targeting malware, VPNFilter, associated with Sandworm Team. US and European government sources linked AcidRain to Russian government entities, while Ukrainian government sources linked AcidRain specifically to Sandworm Team.

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
- S1125: https://attack.mitre.org/software/S1125
- Reviewed: 2026-10-27
