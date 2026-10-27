# Analytic 1292 Technique Platform Profile

## Reference

- Technique: **AN1292 — Analytic 1292**
- Platforms named in the source: macOS

Detects DHCP spoofing by monitoring unified logs for unexpected DHCP ACK/OFFER parameters and correlating with packet captures for multiple DHCP servers. Behavioral emphasis is on inconsistent DNS and gateway assignments that redirect traffic.

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
- AN1292: https://attack.mitre.org/detectionstrategies/DET0468#AN1292
- Reviewed: 2026-10-27
