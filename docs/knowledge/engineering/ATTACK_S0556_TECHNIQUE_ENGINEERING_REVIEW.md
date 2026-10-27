# Pay2Key Technique Engineering Review

## Reference

- Technique: **S0556 — Pay2Key**

Pay2Key is a ransomware written in C++ that has been used by Fox Kitten since at least July 2020 including campaigns against Israeli companies. Pay2Key has been incorporated with a leak site to display stolen sensitive information to further pressure victims into payment.

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
- S0556: https://attack.mitre.org/software/S0556
- Reviewed: 2026-10-27
