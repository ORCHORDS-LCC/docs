# Analytic 1135 Technique Engineering Review

## Reference

- Technique: **AN1135 — Analytic 1135**

Abuse of extended attributes (xattrs) to embed hidden payloads into legitimate files. Defender perspective: detect anomalous use of setfattr or getfattr commands, or direct syscalls (setxattr, getxattr) where attributes are unusually large or contain encoded data. Behavior chain includes: (1) execution of setfattr with suspicious namespaces (user., trusted.), (2) file metadata modification inconsistent with file size/hash, and (3) subsequent process execution reading attributes followed by decoding activity.

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
- AN1135: https://attack.mitre.org/detectionstrategies/DET0406#AN1135
- Reviewed: 2026-10-27
