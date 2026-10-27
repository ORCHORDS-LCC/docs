# Analytic 1554 Technique Platform Profile

## Reference

- Technique: **AN1554 — Analytic 1554**
- Platforms named in the source: ESXi

ESXi hypervisor environmental validation behavioral chain: (1) Virtual machine inventory and configuration enumeration through vim-cmd and esxcli commands, (2) Host hardware and network configuration discovery for hypervisor environment validation, (3) Datastore and storage configuration reconnaissance, (4) vCenter connectivity and cluster membership validation, (5) Selective malware deployment based on virtualization infrastructure characteristics and target VM validation.

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
- AN1554: https://attack.mitre.org/detectionstrategies/DET0562#AN1554
- Reviewed: 2026-10-27
