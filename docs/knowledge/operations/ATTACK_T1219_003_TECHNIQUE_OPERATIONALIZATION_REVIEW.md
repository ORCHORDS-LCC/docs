# Remote Access Hardware Technique Operationalization Review

## Reference

- Technique: **T1219.003 — Remote Access Hardware**

An adversary may use legitimate remote access hardware to establish an interactive command and control channel to target systems within networks. These services, including IP-based keyboard, video, or mouse (KVM) devices such as TinyPilot and PiKVM, are commonly used as legitimate tools and may be allowed by peripheral device policies within a target environment. Remote access hardware may be physically installed and used post-compromise as an alternate communications channel for redundant access or as a way to establish an interactive remote session with the target system. Using hardware-based remote access tools may allow threat actors to bypass software security solutions and gain more control over the compromised device(s).

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
- T1219.003: https://attack.mitre.org/techniques/T1219/003
- Reviewed: 2026-10-27
