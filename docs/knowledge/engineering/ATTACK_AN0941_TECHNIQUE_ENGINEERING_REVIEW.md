# Analytic 0941 Technique Engineering Review

## Reference

- Technique: **AN0941 — Analytic 0941**

Detects the use of message-based injection by monitoring for sequences involving FindWindow (EnumWindows or EnumChildWindows), VirtualAllocEx or related API calls, combined with suspicious PostMessage/SendMessage (e.g., LVM_SETITEMPOSITION) use to SysListView32 controls, followed by LVM_SORTITEMS invocation instead of WriteProcessMemory.

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
- AN0941: https://attack.mitre.org/detectionstrategies/DET0331#AN0941
- Reviewed: 2026-10-27
