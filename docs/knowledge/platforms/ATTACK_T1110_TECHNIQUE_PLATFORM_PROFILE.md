# Brute Force Mitigation Technique Platform Profile

## Reference

- Technique: **T1110 — Brute Force Mitigation**
- Platforms named in the source: not stated

Set account lockout policies after a certain number of failed login attempts to prevent passwords from being guessed. Too strict a policy can create a denial of service condition and render environments un-usable, with all accounts being locked-out permanently. Use multifactor authentication. Follow best practices for mitigating access to Valid Accounts Refer to NIST guidelines when creating passwords. Where possible, also enable multi factor authentication on external facing services.

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
- T1110: https://attack.mitre.org/mitigations/T1110
- Reviewed: 2026-10-27
