# Hypervisor Technique Operationalization Review

## Reference

- Technique: **T1062 — Hypervisor**

**This technique has been deprecated and should no longer be used.** A type-1 hypervisor is a software layer that sits between the guest operating systems and system's hardware. It presents a virtual running environment to an operating system. An example of a common hypervisor is Xen. A type-1 hypervisor operates at a level below the operating system and could be designed with Rootkit functionality to hide its existence from the guest operating system. A malicious hypervisor of this nature could be used to persist on systems through interruption.

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
- T1062: https://attack.mitre.org/techniques/T1062
- Reviewed: 2026-10-27
