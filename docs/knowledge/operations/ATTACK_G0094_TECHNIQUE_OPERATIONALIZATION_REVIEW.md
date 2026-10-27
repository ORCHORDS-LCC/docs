# Kimsuky Technique Operationalization Review

## Reference

- Technique: **G0094 — Kimsuky**

Kimsuky is a Democratic People's Republic of Korea (DPRK)-based cyber espionage group that has been active since at least 2012. The group initially targeted South Korean government agencies, think tanks, and subject-matter experts in various fields. Its operations expanded to include the United Nations and organizations in the government, education, business services, and manufacturing sectors across the United States, Japan, Russia, and Europe. Kimsuky has focused collection on foreign policy and national security issues tied to the Korean Peninsula, nuclear policy, and sanctions. Kimsuky operations have overlapped with those of other North Korean state-sponsored cyber espionage actors as a result of ad hoc collaborations or other limited resource sharing. Kimsuky was assessed to be responsible for the 2014 Korea Hydro & Nuclear Power Co. compromise; other notable campaigns include Operation STOLEN PENCIL (2018), Operation Kabar Cobra (2019), and Operation Smoke Screen (2019). In 2023, Kimsuky was observed using commercial large language models (LLMs) to assist with vulnerability research, scripting, social engineering and reconnaissance. DPRK threat actor cluster boundaries overlap in open source reporting, with some security researchers consolidating all attributed North Korean state-sponsored cyber activity under Lazarus Group, rather than tracking operationally distinct subgroups.

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
- G0094: https://attack.mitre.org/groups/G0094
- Reviewed: 2026-10-27
