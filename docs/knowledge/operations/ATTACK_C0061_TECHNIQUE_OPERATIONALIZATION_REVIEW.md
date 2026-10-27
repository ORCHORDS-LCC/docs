# Operation Digital Eye Technique Operationalization Review

## Reference

- Technique: **C0061 — Operation Digital Eye**

Operation Digital Eye was conducted in June and July of 2024 by suspected People's Republic of China (PRC)-nexus threat actors targeting business-to-business IT service providers in Southern Europe. Operation Digital Eye activity included the use of Visual Studio Code tunnels for command and control (C2) and custom lateral movement capabilities. Overlaps in tooling between Digital Eye and previous China-nexus campaigns, Operation Soft Cell and Operation Tainted Love, indicate the potential use of shared vendors or digital quartermasters.

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
- C0061: https://attack.mitre.org/campaigns/C0061
- Reviewed: 2026-10-27
