# Analytic 0444 Technique Platform Profile

## Reference

- Technique: **AN0444 — Analytic 0444**
- Platforms named in the source: Windows

Detects Kerberoasting attempts by monitoring for anomalous Kerberos TGS requests (Event ID 4769) with RC4 encryption (etype 0x17), accounts requesting an unusual number of service tickets in a short period, or service accounts targeted outside normal usage baselines. Also correlates suspicious process activity (e.g., Mimikatz invoking LSASS access) with Kerberos ticket anomalies.

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
- AN0444: https://attack.mitre.org/detectionstrategies/DET0157#AN0444
- Reviewed: 2026-10-27
