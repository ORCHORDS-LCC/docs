# Analytic 1464 Technique Engineering Review

## Reference

- Technique: **AN1464 — Analytic 1464**

Execution of PubPrn.vbs via cscript.exe using the 'script:' moniker to load and execute a remote .sct scriptlet file, bypassing signature validation and proxying remote payloads through a signed Microsoft script host.

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
- AN1464: https://attack.mitre.org/detectionstrategies/DET0528#AN1464
- Reviewed: 2026-10-27
