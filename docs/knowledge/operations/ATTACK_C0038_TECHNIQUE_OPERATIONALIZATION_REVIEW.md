# HomeLand Justice Technique Operationalization Review

## Reference

- Technique: **C0038 — HomeLand Justice**

HomeLand Justice was a disruptive cyber campaign conducted by Iranian state-affiliated actors against Albanian government networks in July and September 2022. The activity combined ransomware, wiper malware, and data leak operations. Initial access for HomeLand Justice was established as early as May 2021, and threat actors moved laterally, exfiltrated sensitive information, and maintained persistence for approximately 14 months prior to the destructive phase of the operation. Responsibility was claimed by the "HomeLand Justice" front, which framed the campaign as retaliation against the Mujahedeen-e Khalq (MEK), an Iranian opposition group with a presence in Albania. Multiple Iran-nexus groups are assessed to have participated in the campaign, including HEXANE who probed victim infrastructure. A second wave of attacks was launched in September 2022 using similar tactics following public attribution of the previous activity to Iran and the severing of diplomatic ties between Iran and Albania.

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
- C0038: https://attack.mitre.org/campaigns/C0038
- Reviewed: 2026-10-27
