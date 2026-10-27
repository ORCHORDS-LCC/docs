# VersaMem Technique Platform Profile

## Reference

- Technique: **S1154 — VersaMem**
- Platforms named in the source: Network Devices

VersaMem is a web shell designed for deployment to Versa Director servers following exploitation. Discovered in August 2024, VersaMem was used during Versa Director Zero Day Exploitation by Volt Typhoon to target ISPs and MSPs. VersaMem is deployed as a Java Archive (JAR) and allows for credential capture for Versa Director logon activity as well as follow-on execution of arbitrary Java payloads.

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
- S1154: https://attack.mitre.org/software/S1154
- Reviewed: 2026-10-27
