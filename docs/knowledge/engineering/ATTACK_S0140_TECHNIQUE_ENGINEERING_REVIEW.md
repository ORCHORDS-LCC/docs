# Shamoon Technique Engineering Review

## Reference

- Technique: **S0140 — Shamoon**

Shamoon is wiper malware that was first used by an Iranian group known as the "Cutting Sword of Justice" in 2012. Other versions known as Shamoon 2 and Shamoon 3 were observed in 2016 and 2018. Shamoon has also been seen leveraging RawDisk and Filerase to carry out data wiping tasks. Analysis has linked Shamoon with Kwampirs based on multiple shared artifacts and coding patterns. The term Shamoon is sometimes used to refer to the group using the malware as well as the malware itself.

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
- S0140: https://attack.mitre.org/software/S0140
- Reviewed: 2026-10-27
