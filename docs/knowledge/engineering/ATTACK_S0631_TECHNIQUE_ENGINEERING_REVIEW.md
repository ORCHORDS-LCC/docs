# Chaes Technique Engineering Review

## Reference

- Technique: **S0631 — Chaes**

Chaes is a multistage information stealer written in several programming languages that collects login credentials, credit card numbers, and other financial information. Chaes was first observed in 2020, and appears to primarily target victims in Brazil as well as other e-commerce customers in Latin America.

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
- S0631: https://attack.mitre.org/software/S0631
- Reviewed: 2026-10-27
