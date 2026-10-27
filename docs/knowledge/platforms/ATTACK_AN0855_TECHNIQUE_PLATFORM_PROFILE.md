# Analytic 0855 Technique Platform Profile

## Reference

- Technique: **AN0855 — Analytic 0855**
- Platforms named in the source: Network Devices

Defender observes configuration changes on firewall/network appliance involving rule creation, modification, or deletion from abnormal management IPs or non-console channels (e.g., remote CLI, API). These are often correlated with a spike in previously blocked outbound traffic, unexpected allow-all rules, or bulk rule deletions. Behavior often follows unauthorized login, privilege escalation, or API abuse.

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
- AN0855: https://attack.mitre.org/detectionstrategies/DET0306#AN0855
- Reviewed: 2026-10-27
