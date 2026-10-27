# CorKLOG Technique Engineering Review

## Reference

- Technique: **S1235 — CorKLOG**

CorKLOG is a keylogger known to be leveraged by Mustang Panda and was first observed utilized in 2024. CorKLOG is delivered through a RAR archive (e.g., src.rar), which contains two files: an executable (lcommute.exe) and the CorKLOG DLL (mscorsvc.dll). CorKLOG has established persistence on the system by creating services or with scheduled tasks.

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
- S1235: https://attack.mitre.org/software/S1235
- Reviewed: 2026-10-27
