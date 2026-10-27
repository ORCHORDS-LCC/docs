# Analytic 1502 Technique Platform Profile

## Reference

- Technique: **AN1502 — Analytic 1502**
- Platforms named in the source: IaaS

Monitor for suspicious use of cloud-native administrative command services (e.g., AWS Systems Manager Run Command, Azure RunCommand, GCP OS Config) to execute code inside VMs. Detect anomalies such as commands/scripts executed by unexpected users, execution outside of maintenance windows, or commands initiated by service accounts not normally tied to administration. Correlate cloud control-plane activity logs with host-level execution (process creation, script execution) to validate if commands materialized inside the guest OS.

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
- AN1502: https://attack.mitre.org/detectionstrategies/DET0545#AN1502
- Reviewed: 2026-10-27
