# Analytic 0274 Technique Platform Profile

## Reference

- Technique: **AN0274 — Analytic 0274**
- Platforms named in the source: Windows

Behavioral chain: (1) An actor creates or modifies a BITS job via bitsadmin.exe, PowerShell BITS cmdlets, or COM; (2) the job performs HTTP(S)/SMB network transfers while the owning user is logged on; (3) upon job completion/error, BITS launches a notify command (SetNotifyCmdLine) from svchost.exe -k netsvcs -s BITS, often establishing persistence by keeping long-lived jobs. The strategy correlates process creation, command/script telemetry, BITS-Client operational events, and network connections initiated by BITS.

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
- AN0274: https://attack.mitre.org/detectionstrategies/DET0098#AN0274
- Reviewed: 2026-10-27
