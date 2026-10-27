# Analytic 1177 Technique Engineering Review

## Reference

- Technique: **AN1177 — Analytic 1177**

Multi-stage Windows DACL manipulation behavioral chain: (1) Process creation of permission-modifying utilities (icacls.exe, takeown.exe, attrib.exe, cacls.exe) or PowerShell ACL cmdlets, (2) Command-line analysis revealing privilege escalation intent through suspicious parameters (/grant, /takeown, /T, Set-Acl), (3) DACL modification events (4670) correlating with process execution, (4) Subsequent file access attempts (4663) indicating successful permission bypass, (5) Potential follow-on persistence or lateral movement activities.

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
- AN1177: https://attack.mitre.org/detectionstrategies/DET0418#AN1177
- Reviewed: 2026-10-27
