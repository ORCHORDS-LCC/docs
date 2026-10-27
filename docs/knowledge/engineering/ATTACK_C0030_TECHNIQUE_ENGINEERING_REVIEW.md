# Triton Safety Instrumented System Attack Technique Engineering Review

## Reference

- Technique: **C0030 — Triton Safety Instrumented System Attack**

Triton Safety Instrumented System Attack was a campaign employed by TEMP.Veles which leveraged the Triton malware framework against a petrochemical organization. The malware and techniques used within this campaign targeted specific Triconex Safety Controllers within the environment. The incident was eventually discovered due to a safety trip that occurred as a result of an issue in the malware.

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
- C0030: https://attack.mitre.org/campaigns/C0030
- Reviewed: 2026-10-27
