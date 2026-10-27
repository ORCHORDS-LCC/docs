# BPFDoor Technique Operationalization Review

## Reference

- Technique: **S1161 — BPFDoor**

BPFDoor is a Linux based passive long-term backdoor used by China-based threat actors. First seen in 2021, BPFDoor is named after its usage of Berkley Packet Filter (BPF) to execute single task instructions. BPFDoor supports multiple protocols for communicating with a C2 including TCP, UDP, and ICMP and can start local or reverse shells that bypass firewalls using iptables.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- S1161: https://attack.mitre.org/software/S1161
- Reviewed: 2026-10-27
