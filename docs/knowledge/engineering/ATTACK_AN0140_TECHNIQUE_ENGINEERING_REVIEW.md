# Analytic 0140 Technique Engineering Review

## Reference

- Technique: **AN0140 — Analytic 0140**

Adversaries writing or moving payloads into directories configured as AV/EDR exclusion paths (e.g., /tmp, /var/lib, or custom directories from auditd exclusion rules). Defender perspective: detect file creation in paths matching known exclusions correlated with unusual parent processes.

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
- AN0140: https://attack.mitre.org/detectionstrategies/DET0051#AN0140
- Reviewed: 2026-10-27
