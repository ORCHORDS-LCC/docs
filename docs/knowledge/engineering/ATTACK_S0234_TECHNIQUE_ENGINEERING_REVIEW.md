# Bandook Technique Engineering Review

## Reference

- Technique: **S0234 — Bandook**

Bandook is a commercially available RAT, written in Delphi and C++, that has been available since at least 2007. It has been used against government, financial, energy, healthcare, education, IT, and legal organizations in the US, South America, Europe, and Southeast Asia. Bandook has been used by Dark Caracal, as well as in a separate campaign referred to as "Operation Manul".

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
- S0234: https://attack.mitre.org/software/S0234
- Reviewed: 2026-10-27
