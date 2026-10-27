# Network Devices Technique Operationalization Review

## Reference

- Technique: **T1584.008 — Network Devices**

Adversaries may compromise third-party network devices that can be used during targeting. Network devices, such as small office/home office (SOHO) routers, may be compromised where the adversary's ultimate goal is not Initial Access to that environment, but rather to leverage these devices to support additional targeting. Once an adversary has control, compromised network devices can be used to launch additional operations, such as hosting payloads for Phishing campaigns (i.e., Link Target) or enabling the required access to execute Content Injection operations. Adversaries may also be able to harvest reusable credentials (i.e., Valid Accounts) from compromised network devices. Adversaries often target Internet-facing edge devices and related network appliances that specifically do not support robust host-based defenses. Compromised network devices may be used to support subsequent Command and Control activity, such as Hide Infrastructure through an established Proxy and/or Botnet network.

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
- T1584.008: https://attack.mitre.org/techniques/T1584/008
- Reviewed: 2026-10-27
