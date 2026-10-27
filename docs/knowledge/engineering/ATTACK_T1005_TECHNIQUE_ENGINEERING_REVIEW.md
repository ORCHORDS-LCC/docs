# Data from Local System Technique Engineering Review

## Reference

- Technique: **T1005 — Data from Local System**

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration. Adversaries may do this using a Command and Scripting Interpreter, such as cmd as well as a Network Device CLI, which have functionality to interact with the file system to gather information. Adversaries may also use Automated Collection on the local system.

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
- T1005: https://attack.mitre.org/techniques/T1005
- Reviewed: 2026-10-27
