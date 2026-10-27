# Analytic 1356 Technique Platform Profile

## Reference

- Technique: **AN1356 — Analytic 1356**
- Platforms named in the source: IaaS

Defenders should monitor for anomalous or unauthorized changes to cloud compute configurations that alter quotas, tenant-wide policies, subscription associations, or allowed deployment regions. From a defender’s perspective, suspicious behavior chains include a sudden increase in compute quota requests followed by new instance or resource creation, policy modifications that weaken security restrictions, or enabling previously unused/unsupported cloud regions. Correlation across identity, configuration, and subsequent provisioning logs is critical to distinguish legitimate administrative activity from adversarial abuse.

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
- AN1356: https://attack.mitre.org/detectionstrategies/DET0492#AN1356
- Reviewed: 2026-10-27
