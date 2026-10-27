# KV Botnet Activity Technique Operationalization Review

## Reference

- Technique: **C0035 — KV Botnet Activity**

KV Botnet Activity consisted of exploitation of primarily “end-of-life” small office-home office (SOHO) equipment from manufacturers such as Cisco, NETGEAR, and DrayTek. KV Botnet Activity was used by Volt Typhoon to obfuscate connectivity to victims in multiple critical infrastructure segments, including energy and telecommunication companies and entities based on the US territory of Guam. While the KV Botnet is the most prominent element of this campaign, it overlaps with another botnet cluster referred to as the JDY cluster. This botnet was disrupted by US law enforcement entities in early 2024 after periods of activity from October 2022 through January 2024.

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
- C0035: https://attack.mitre.org/campaigns/C0035
- Reviewed: 2026-10-27
