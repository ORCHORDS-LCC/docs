# Raspberry Robin Technique Platform Profile

## Reference

- Technique: **S1130 — Raspberry Robin**
- Platforms named in the source: Windows

Raspberry Robin is initial access malware first identified in September 2021, and active through early 2024. The malware is notable for spreading via infected USB devices containing a malicious LNK object that, on execution, retrieves remote hosted payloads for installation. Raspberry Robin has been widely used against various industries and geographies, and as a precursor to information stealer, ransomware, and other payloads such as SocGholish, Cobalt Strike, IcedID, and Bumblebee. The DLL componenet in the Raspberry Robin infection chain is also referred to as "Roshtyak." The name "Raspberry Robin" is used to refer to both the malware as well as the threat actor associated with its use, although the Raspberry Robin operators are also tracked as Storm-0856 by some vendors.

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
- S1130: https://attack.mitre.org/software/S1130
- Reviewed: 2026-10-27
