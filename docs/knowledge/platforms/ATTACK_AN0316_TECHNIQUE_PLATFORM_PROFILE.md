# Analytic 0316 Technique Platform Profile

## Reference

- Technique: **AN0316 — Analytic 0316**
- Platforms named in the source: Windows

Detects AS-REP roasting attempts by monitoring for Kerberos AS-REQ/AS-REP authentication patterns where preauthentication is disabled (Event ID 4768 with Pre-Auth Type 0). Correlates these requests with subsequent service ticket activity (Event ID 4769) and anomalies such as requests using weak RC4 encryption (etype 0x17). Excessive enumeration of accounts with 'Do not require Kerberos preauthentication' set in Active Directory is another key detection point.

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
- AN0316: https://attack.mitre.org/detectionstrategies/DET0113#AN0316
- Reviewed: 2026-10-27
