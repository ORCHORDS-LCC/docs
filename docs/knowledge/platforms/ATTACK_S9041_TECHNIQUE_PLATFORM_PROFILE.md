# TeamPCP Cloud Stealer Technique Platform Profile

## Reference

- Technique: **S9041 — TeamPCP Cloud Stealer**
- Platforms named in the source: Containers, Linux, macOS, SaaS, Windows

The TeamPCP Cloud Stealer is a comprehensive filesystem credential stealer that can harvest, encrypt, and exfiltrate credentials from over 50 sensitive file paths across CI/CD, cloud, developer tooling, and container environments. The TeamPCP Cloud Stealer was the primary payload used by TeamPCP in March 2026 during early stages of a cascading supply chain campaign targeting CI/CD workflows.

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
- S9041: https://attack.mitre.org/software/S9041
- Reviewed: 2026-10-27
