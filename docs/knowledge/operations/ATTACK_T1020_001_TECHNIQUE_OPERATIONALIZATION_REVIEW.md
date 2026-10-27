# Traffic Duplication Technique Operationalization Review

## Reference

- Technique: **T1020.001 — Traffic Duplication**

Adversaries may leverage traffic mirroring in order to automate data exfiltration over compromised infrastructure. Traffic mirroring is a native feature for some devices, often used for network analysis. For example, devices may be configured to forward network traffic to one or more destinations for analysis by a network analyzer or other monitoring device. Adversaries may abuse traffic mirroring to mirror or redirect network traffic through other infrastructure they control. Malicious modifications to network devices to enable traffic redirection may be possible through ROMMONkit or Patch System Image. Many cloud-based environments also support traffic mirroring. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to. Adversaries may use traffic duplication in conjunction with Network Sniffing, Input Capture, or Adversary-in-the-Middle depending on the goals and objectives of the adversary.

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
- T1020.001: https://attack.mitre.org/techniques/T1020/001
- Reviewed: 2026-10-27
