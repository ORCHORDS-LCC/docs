# Tsundere Botnet Technique Operationalization Review

## Reference

- Technique: **S9034 — Tsundere Botnet**

Tsundere Botnet is a botnet first reported in mid-2025 that is delivered via MSI installer or a PowerShell script. It leverages Node.js and JavaScript for payload delivery and execution, and uses smart contracts on the blockchain to host command and control (C2) addresses. Tsundere Botnet is attributed to a likely Russian-speaking threat actor. A variant named DinDoor has been linked to MuddyWater operations and uses the Deno runtime for execution rather than Node.js.

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
- S9034: https://attack.mitre.org/software/S9034
- Reviewed: 2026-10-27
