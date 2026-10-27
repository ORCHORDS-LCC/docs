# Gootloader Technique Engineering Review

## Reference

- Technique: **S1138 — Gootloader**

Gootloader is a Javascript-based infection framework that has been used since at least 2020 as a delivery method for the Gootkit banking trojan, Cobalt Strike, REvil, and others. Gootloader operates on an "Initial Access as a Service" model and has leveraged SEO Poisoning to provide access to entities in multiple sectors worldwide including financial, military, automotive, pharmaceutical, and energy.

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
- S1138: https://attack.mitre.org/software/S1138
- Reviewed: 2026-10-27
