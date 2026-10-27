# Control Panel Items Mitigation Technique Engineering Review

## Reference

- Technique: **T1196 — Control Panel Items Mitigation**

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating specific Windows API calls and/or execution of particular file extensions will likely have unintended side effects, such as preventing legitimate software (i.e., drivers and configuration tools) from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior. Restrict storage and execution of Control Panel items to protected directories, such as C:\Windows, rather than user directories. Index known safe Control Panel items and block potentially malicious software using whitelisting tools like AppLocker that are capable of auditing and/or blocking unknown executable files. Consider fully enabling User Account Control (UAC) to impede system-wide changes from illegitimate administrators.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1196: https://attack.mitre.org/mitigations/T1196
- Reviewed: 2026-10-27
