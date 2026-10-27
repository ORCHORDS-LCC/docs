# cd00r Technique Engineering Review

## Reference

- Technique: **S1204 — cd00r**

Cd00r is an open-source backdoor for UNIX and UNIX-variant operating systems that was orginally released in 2000. cd00r source code is primarily based on a packet-capturing program as it utilizes a sniffer to listen for specific sequences of network traffic or "secret knock" before executing the attacker's code.

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
- S1204: https://attack.mitre.org/software/S1204
- Reviewed: 2026-10-27
