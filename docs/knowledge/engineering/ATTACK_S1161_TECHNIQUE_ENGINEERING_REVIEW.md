# BPFDoor Technique Engineering Review

## Reference

- Technique: **S1161 — BPFDoor**

BPFDoor is a Linux based passive long-term backdoor used by China-based threat actors. First seen in 2021, BPFDoor is named after its usage of Berkley Packet Filter (BPF) to execute single task instructions. BPFDoor supports multiple protocols for communicating with a C2 including TCP, UDP, and ICMP and can start local or reverse shells that bypass firewalls using iptables.

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
- S1161: https://attack.mitre.org/software/S1161
- Reviewed: 2026-10-27
