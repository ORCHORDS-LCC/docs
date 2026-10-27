# Third-party Software Mitigation Technique Platform Profile

## Reference

- Technique: **T1072 — Third-party Software Mitigation**
- Platforms named in the source: not stated

Evaluate the security of third-party software that could be used in the enterprise environment. Ensure that access to management systems for third-party systems is limited, monitored, and secure. Have a strict approval policy for use of third-party systems. Grant access to Third-party systems only to a limited number of authorized administrators. Ensure proper system and access isolation for critical network systems through use of firewalls, account privilege separation, group policy, and multi-factor authentication. Verify that account credentials that may be used to access third-party systems are unique and not used throughout the enterprise network. Ensure that any accounts used by third-party providers to access these systems are traceable to the third-party and are not used throughout the network or used by other third-party providers in the same environment. Ensure third-party systems are regularly patched by users or the provider to prevent potential remote access through Exploitation for Privilege Escalation. Ensure there are regular reviews of accounts provisioned to these systems to verify continued business need, and ensure there is governance to trace de-provisioning of access that is no longer required. Where the third-party system is used for deployment services, ensure that it can be configured to deploy only signed binaries, then ensure that the trusted signing certificates are not co-located with the third-party system and are instead located on a system that cannot be accessed remotely or to which remote access is tightly controlled.

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
- T1072: https://attack.mitre.org/mitigations/T1072
- Reviewed: 2026-10-27
