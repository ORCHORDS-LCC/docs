# Compile After Delivery Mitigation Technique Platform Profile

## Reference

- Technique: **T1500 — Compile After Delivery Mitigation**
- Platforms named in the source: not stated

This type of technique cannot be easily mitigated with preventive controls or patched since it is based on the abuse of operating system design features. For example, blocking all file compilation may have unintended side effects, such as preventing legitimate OS frameworks and code development mechanisms from operating properly. Consider removing compilers if not needed, otherwise efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior. Identify unnecessary system utilities or potentially malicious software that may be used to decrypt, deobfuscate, decode, and compile files or information, and audit and/or block them by using whitelisting tools, like AppLocker, or Software Restriction Policies where appropriate.

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
- T1500: https://attack.mitre.org/mitigations/T1500
- Reviewed: 2026-10-27
