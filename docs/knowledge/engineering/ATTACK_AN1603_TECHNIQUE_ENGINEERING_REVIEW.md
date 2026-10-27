# Analytic 1603 Technique Engineering Review

## Reference

- Technique: **AN1603 — Analytic 1603**

Detection of unauthorized changes to boot configurations pointing to TFTP servers, unusual firmware loads during netbooting, or suspicious TFTP traffic. Correlation of boot config modifications, command history logs, and unexpected system image hashes provides detection coverage for adversaries attempting to persist via malicious TFTP boot images.

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
- AN1603: https://attack.mitre.org/detectionstrategies/DET0582#AN1603
- Reviewed: 2026-10-27
