# Analytic 1075 Technique Platform Profile

## Reference

- Technique: **AN1075 — Analytic 1075**
- Platforms named in the source: Windows

Correlates file enumeration of XML files in the SYSVOL share with suspicious process execution that decodes or reads encrypted credentials embedded in Group Policy Preference files (e.g., Get-GPPPassword.ps1, gpprefdecrypt.py, Metasploit). Detects abnormal access to \DOMAIN\SYSVOL combined with XML file parsing or decryption logic.

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
- AN1075: https://attack.mitre.org/detectionstrategies/DET0381#AN1075
- Reviewed: 2026-10-27
