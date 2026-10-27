# Local Account Technique Engineering Review

## Reference

- Technique: **T1087.001 — Local Account**

Adversaries may attempt to get a listing of local system accounts. This information can help adversaries determine which local accounts exist on a system to aid in follow-on behavior. Commands such as net user and net localgroup of the Net utility and id and groups on macOS and Linux can list local users and groups. On Linux, local users can also be enumerated through the use of the /etc/passwd file. On macOS, the dscl . list /Users command can be used to enumerate local accounts. On ESXi servers, the `esxcli system account list` command can list local user accounts.

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
- T1087.001: https://attack.mitre.org/techniques/T1087/001
- Reviewed: 2026-10-27
