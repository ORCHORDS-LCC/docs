# Rising Sun Technique Engineering Review

## Reference

- Technique: **S0448 — Rising Sun**

Rising Sun is a modular backdoor that was used extensively in Operation Sharpshooter between 2017 and 2019. Rising Sun infected at least 87 organizations around the world, including nuclear, defense, energy, and financial service companies. Security researchers assessed Rising Sun included some source code from Lazarus Group's Trojan Duuzer.

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
- S0448: https://attack.mitre.org/software/S0448
- Reviewed: 2026-10-27
