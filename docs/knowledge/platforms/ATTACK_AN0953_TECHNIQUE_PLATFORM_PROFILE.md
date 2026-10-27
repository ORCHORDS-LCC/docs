# Analytic 0953 Technique Platform Profile

## Reference

- Technique: **AN0953 — Analytic 0953**
- Platforms named in the source: IaaS

Defenders can detect suspicious reversion of cloud compute instances by monitoring for unusual snapshot restores, rollback actions, or ephemeral storage resets that occur outside expected administrative workflows. From a defender’s perspective, relevant detection chains include: a snapshot restore triggered by a new or rarely used account, a sequence of snapshot creation immediately followed by a restore and instance start, or rollbacks performed from anomalous geographic or network locations. These patterns may indicate attempts to remove forensic evidence or re-establish a clean execution state for persistence.

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
- AN0953: https://attack.mitre.org/detectionstrategies/DET0337#AN0953
- Reviewed: 2026-10-27
