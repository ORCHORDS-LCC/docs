# Industroyer2 Technique Platform Profile

## Reference

- Technique: **S1072 — Industroyer2**
- Platforms named in the source: Field Controller/RTU/PLC/IED, Engineering Workstation

Industroyer2 is a compiled and static piece of malware that has the ability to communicate over the IEC-104 protocol. It is similar to the IEC-104 module found in Industroyer. Security researchers assess that Industroyer2 was designed to cause impact to high-voltage electrical substations. The initial Industroyer2 sample was compiled on 03/23/2022 and scheduled to execute on 04/08/2022, however it was discovered before deploying, resulting in no impact.

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
- S1072: https://attack.mitre.org/software/S1072
- Reviewed: 2026-10-27
