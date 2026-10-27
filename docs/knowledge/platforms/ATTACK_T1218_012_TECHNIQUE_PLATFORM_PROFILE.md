# Verclsid Technique Platform Profile

## Reference

- Technique: **T1218.012 — Verclsid**
- Platforms named in the source: Windows

Adversaries may abuse verclsid.exe to proxy execution of malicious code. Verclsid.exe is known as the Extension CLSID Verification Host and is responsible for verifying each shell extension before they are used by Windows Explorer or the Windows Shell. Adversaries may abuse verclsid.exe to execute malicious payloads. This may be achieved by running <code>verclsid.exe /S /C {CLSID}</code>, where the file is referenced by a Class ID (CLSID), a unique identification number used to identify COM objects. COM payloads executed by verclsid.exe may be able to perform various malicious actions, such as loading and executing COM scriptlets (SCT) from remote servers (similar to Regsvr32). Since the binary may be signed and/or native on Windows systems, proxying execution via verclsid.exe may bypass application control solutions that do not account for its potential abuse.

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
- T1218.012: https://attack.mitre.org/techniques/T1218/012
- Reviewed: 2026-10-27
