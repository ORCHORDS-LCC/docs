# Mini Shai-Hulud Technique Platform Profile

## Reference

- Technique: **S9043 — Mini Shai-Hulud**
- Platforms named in the source: Containers, IaaS, Linux, macOS, SaaS, Windows

Mini Shai-Hulud is a credential stealer and self-replicating supply chain worm, derived from Shai-Hulud, that has been used by TeamPCP to target Continuous Integration and Continuous Delivery/Deployment (CI/CD) workflows since at least 2026. Mini Shai-Hulud can compromise credentials across multiple cloud, container, and AI configuration file paths and can use stolen npm and GitHub OIDC tokens to spread to other packages maintained by the compromised user. Mini Shai-Hulud also has a targeted wiper component and has used multiple C2 and data exfiltration mechanisms.

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
- S9043: https://attack.mitre.org/software/S9043
- Reviewed: 2026-10-27
