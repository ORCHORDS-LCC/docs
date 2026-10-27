# Logon Scripts Mitigation Technique Platform Profile

## Reference

- Technique: **T1037 — Logon Scripts Mitigation**
- Platforms named in the source: not stated

Restrict write access to logon scripts to specific administrators. Prevent access to administrator accounts by mitigating Credential Access techniques and limiting account access and permissions of Valid Accounts. Identify and block potentially malicious software that may be executed through logon script modification by using whitelisting tools like AppLocker that are capable of auditing and/or blocking unknown programs.

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
- T1037: https://attack.mitre.org/mitigations/T1037
- Reviewed: 2026-10-27
