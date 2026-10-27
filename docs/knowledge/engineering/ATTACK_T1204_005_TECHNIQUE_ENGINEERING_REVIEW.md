# Malicious Library Technique Engineering Review

## Reference

- Technique: **T1204.005 — Malicious Library**

Adversaries may rely on a user installing a malicious library to facilitate execution. Threat actors may Upload Malware to package managers such as NPM and PyPi, as well as to public code repositories such as GitHub. User may install libraries without realizing they are malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that establishes persistence, steals data, or mines cryptocurrency. In some cases, threat actors may compromise and backdoor existing popular libraries (i.e., Compromise Software Dependencies and Development Tools). Alternatively, they may create entirely new packages and leverage behaviors such as typosquatting to encourage users to install them.

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
- T1204.005: https://attack.mitre.org/techniques/T1204/005
- Reviewed: 2026-10-27
