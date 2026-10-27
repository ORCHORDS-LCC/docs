# Analytic 0647 Technique Platform Profile

## Reference

- Technique: **AN0647 — Analytic 0647**
- Platforms named in the source: Network Devices

Defenders may observe adversary attempts to collect or export full device configurations by detecting unusual SNMP queries, Smart Install (SMI) activity, or CLI/API commands that request running or startup configuration dumps. Correlated behaviors include high-volume read requests for sensitive OIDs, repeated use of 'show running-config' or equivalent commands from untrusted IPs, or unexpected TFTP/SCP/FTP transfers containing configuration files. These behaviors often appear in sequence: anomalous authentication or privilege escalation, followed by bulk configuration retrieval and outbound transfer.

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
- AN0647: https://attack.mitre.org/detectionstrategies/DET0233#AN0647
- Reviewed: 2026-10-27
