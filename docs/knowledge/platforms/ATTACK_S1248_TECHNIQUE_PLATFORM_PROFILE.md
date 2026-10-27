# XORIndex Loader Technique Platform Profile

## Reference

- Technique: **S1248 — XORIndex Loader**
- Platforms named in the source: Windows

XORIndex Loader is a XOR-encoded loader that collects host data, decodes follow-on scripts and acts as a downloader for the BeaverTail malware. XORIndex Loader was first reported in June 2025. XORIndex Loader has been leveraged by North Korea-affiliated threat actors identified as Contagious Interview. XORIndex Loader has been delivered to victims through code repository sites utilizing typo squatting naming conventions of various npm packages.

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
- S1248: https://attack.mitre.org/software/S1248
- Reviewed: 2026-10-27
