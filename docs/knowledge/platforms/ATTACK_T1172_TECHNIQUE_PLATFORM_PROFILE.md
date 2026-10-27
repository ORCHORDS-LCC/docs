# Domain Fronting Mitigation Technique Platform Profile

## Reference

- Technique: **T1172 — Domain Fronting Mitigation**
- Platforms named in the source: not stated

If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be Domain Fronting. In order to use domain fronting, attackers will likely need to deploy additional tools to compromised systems. It may be possible to detect or prevent the installation of these tools with Host-based solutions.

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
- T1172: https://attack.mitre.org/mitigations/T1172
- Reviewed: 2026-10-27
