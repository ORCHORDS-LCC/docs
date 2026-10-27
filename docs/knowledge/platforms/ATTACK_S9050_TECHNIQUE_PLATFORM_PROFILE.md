# Vidar Technique Platform Profile

## Reference

- Technique: **S9050 — Vidar**
- Platforms named in the source: Windows

Vidar is a Windows infostealer that was first advertised in November 2018. Written in C++, Vidar collects PII, cryptocurrency wallets, documents and other data within the compromised machine. Version 2 of Vidar was published in October 2025, and has been used in numerous operations since its release. Vidar has been observed alongside other malware strains, including STOP/Djvu ransomware, Mina.exe (an XMRIG miner), and Clip1.exe (a Laplas Clipper sample).

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
- S9050: https://attack.mitre.org/software/S9050
- Reviewed: 2026-10-27
