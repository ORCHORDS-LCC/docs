# Analytic 1144 Technique Platform Profile

## Reference

- Technique: **AN1144 — Analytic 1144**
- Platforms named in the source: Windows

Detects anomalous NTLM LogonType 3 authentications that occur without accompanying domain logon events, especially from lateral systems or involving built-in administrative tools. Monitors for mismatches between source user context and system being accessed. Correlates LogonSession creation, NTLM authentications, and process/service initiation to identify suspicious use of stolen password hashes for remote access or service logon without password entry. Detects overpass-the-hash by combining Kerberos ticket issuance with NTLM-based lateral movement.

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
- AN1144: https://attack.mitre.org/detectionstrategies/DET0409#AN1144
- Reviewed: 2026-10-27
