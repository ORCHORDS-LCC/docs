# Password Policy Discovery Mitigation Technique Platform Profile

## Reference

- Technique: **T1201 — Password Policy Discovery Mitigation**
- Platforms named in the source: not stated

Mitigating discovery of password policies is not advised since the information is required to be known by systems and users of a network. Ensure password policies are such that they mitigate brute force attacks yet will not give an adversary an information advantage because the policies are too light. Active Directory is a common way to set and enforce password policies throughout an enterprise network.

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
- T1201: https://attack.mitre.org/mitigations/T1201
- Reviewed: 2026-10-27
