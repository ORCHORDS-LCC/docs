# Dridex Technique Engineering Review

## Reference

- Technique: **S0384 — Dridex**

Dridex is a prolific banking Trojan that first appeared in 2014. By December 2019, the US Treasury estimated Dridex had infected computers in hundreds of banks and financial institutions in over 40 countries, leading to more than $100 million in theft. Dridex was created from the source code of the Bugat banking Trojan (also known as Cridex).

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
- S0384: https://attack.mitre.org/software/S0384
- Reviewed: 2026-10-27
