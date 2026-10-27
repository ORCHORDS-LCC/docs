# PUBLOAD Technique Platform Profile

## Reference

- Technique: **S1228 — PUBLOAD**
- Platforms named in the source: Windows

PUBLOAD is a stager malware that has been observed installing itself in existing directories such as `C:\Users\Public` or creating new directories to stage the malware and its components. PUBLOAD malware collects details of the victim host, establishes persistence, encrypts victim details using RC4 and communicates victim details back to C2. PUBLOAD malware has previously been leveraged by China-affiliated actors identified as Mustang Panda. PUBLOAD is also known as “NoFive” and some public reporting identifies the loader component as CLAIMLOADER.

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
- S1228: https://attack.mitre.org/software/S1228
- Reviewed: 2026-10-27
