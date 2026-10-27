# Exploitation for Defense Impairment Technique Engineering Review

## Reference

- Technique: **T1687 — Exploitation for Defense Impairment**

Adversaries may exploit vulnerabilities in security software, infrastructure, or defensive components to degrade, disable, or otherwise continue to impair their ability to prevent, detect, or respond to malicious activity. Adversaries may exploit a system or application vulnerability to directly interfere with defensive mechanisms. Exploitation occurs when an adversary takes advantage of a programming error in software, services, or the operating system to execute adversary-controlled code, often with the goal of weakening or disabling protections. Vulnerabilities may exist in security tools such as antivirus, endpoint detection and response (EDR), firewalls, or other monitoring solutions. Adversaries may use prior reconnaissance or perform discovery activities (e.g., Software Discovery) to identify defensive tools present in an environment and target them for exploitation. Successful exploitation may allow adversaries to terminate security processes, disable protections, bypass enforcement mechanisms, or reduce the effectiveness of defensive controls. In some cases, vulnerabilities in cloud-based or SaaS infrastructure may also be leveraged to bypass built-in security boundaries or disrupt visibility and enforcement across environments.

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
- T1687: https://attack.mitre.org/techniques/T1687
- Reviewed: 2026-10-27
