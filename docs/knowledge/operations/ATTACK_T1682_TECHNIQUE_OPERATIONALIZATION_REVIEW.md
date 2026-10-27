# Query Public AI Services Technique Operationalization Review

## Reference

- Technique: **T1682 — Query Public AI Services**

Adversaries may query publicly accessible artificial intelligence (AI) services, such as large language models (LLMs), to support targeting and operations. In addition to searching websites or databases directly (i.e., Search Open Websites/Domains), adversaries may use AI services to synthesize, aggregate, and analyze publicly available information at scale. This may include identifying individuals or organizations to target, researching organizational structures and personnel, identifying technologies used by target organizations, researching business relationships to develop plausible pretexts for Social Engineering approaches, identifying contact information for use in Phishing or Phishing for Information, or gathering derogatory or sensitive information about individuals that may be used for extortion or coercion. Information gathered through AI services may be leveraged for other behaviors, such as establishing operational resources (i.e., Generate Content or Establish Accounts. For obtaining access to AI tools and services, see Artificial Intelligence.

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
- T1682: https://attack.mitre.org/techniques/T1682
- Reviewed: 2026-10-27
