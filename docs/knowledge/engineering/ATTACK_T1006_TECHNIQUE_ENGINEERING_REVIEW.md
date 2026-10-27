# Direct Volume Access Technique Engineering Review

## Reference

- Technique: **T1006 — Direct Volume Access**

Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell. Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and esentutl) to create shadow copies or backups of data from system volumes.

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
- T1006: https://attack.mitre.org/techniques/T1006
- Reviewed: 2026-10-27
