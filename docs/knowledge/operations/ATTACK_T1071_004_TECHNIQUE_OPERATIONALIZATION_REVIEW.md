# DNS Technique Operationalization Review

## Reference

- Technique: **T1071.004 — DNS**

Adversaries may communicate using the Domain Name System (DNS) application layer protocol to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. The DNS protocol serves an administrative function in computer networking and thus may be very common in environments. DNS traffic may also be allowed even before network authentication is completed. DNS packets contain many fields and headers in which data can be concealed. Often known as DNS tunneling, adversaries may abuse DNS to communicate with systems under their control within a victim network while also mimicking normal, expected traffic. DNS beaconing may be used to send commands to remote systems via DNS queries. A DNS beacon is created by tunneling DNS traffic (i.e. Protocol Tunneling). The commands may be embedded into different DNS records, for example, TXT or A records. DNS beacons may be difficult to detect because the beacons infrequently communicate with infected devices. Infrequent communication conceals the malicious DNS traffic with normal DNS traffic.

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
- T1071.004: https://attack.mitre.org/techniques/T1071/004
- Reviewed: 2026-10-27
