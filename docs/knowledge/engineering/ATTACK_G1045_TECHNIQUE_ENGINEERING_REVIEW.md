# Salt Typhoon Technique Engineering Review

## Reference

- Technique: **G1045 — Salt Typhoon**

Salt Typhoon is a People's Republic of China (PRC) state-backed actor that has been active since at least 2019 and responsible for numerous compromises of network infrastructure at major U.S. telecommunication and internet service providers (ISP). Salt Typhoon has targeted and leveraged public facing network edge devices to gain access to victim environments. Salt Typhoon has been publicly associated with activities resembling other security industry reported activity groups to include OPERATOR PANDA, RedMike, GhostEmperor, and UNC5807.

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
- G1045: https://attack.mitre.org/groups/G1045
- Reviewed: 2026-10-27
