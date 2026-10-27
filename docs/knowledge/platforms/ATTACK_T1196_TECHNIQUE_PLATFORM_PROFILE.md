# Control Panel Items Mitigation Technique Platform Profile

## Reference

- Technique: **T1196 — Control Panel Items Mitigation**
- Platforms named in the source: not stated

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating specific Windows API calls and/or execution of particular file extensions will likely have unintended side effects, such as preventing legitimate software (i.e., drivers and configuration tools) from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior. Restrict storage and execution of Control Panel items to protected directories, such as <code>C:\Windows</code>, rather than user directories. Index known safe Control Panel items and block potentially malicious software using whitelisting tools like AppLocker that are capable of auditing and/or blocking unknown executable files. Consider fully enabling User Account Control (UAC) to impede system-wide changes from illegitimate administrators.

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
- T1196: https://attack.mitre.org/mitigations/T1196
- Reviewed: 2026-10-27
