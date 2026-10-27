# Analytic 1305 Technique Engineering Review

## Reference

- Technique: **AN1305 — Analytic 1305**

Windows-specific environmental keying behavioral chain: (1) Rapid system information discovery through multiple techniques (WMI queries, registry enumeration, network share discovery, hostname/domain checks), (2) Target validation through specific environmental artifact collection (AD domain membership, network topology, installed software versions), (3) Cryptographic operation correlation indicating payload decryption based on collected environmental values, (4) Subsequent malicious code execution following successful environmental validation, (5) Temporal clustering of discovery activities suggesting automated environmental assessment.

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
- AN1305: https://attack.mitre.org/detectionstrategies/DET0474#AN1305
- Reviewed: 2026-10-27
