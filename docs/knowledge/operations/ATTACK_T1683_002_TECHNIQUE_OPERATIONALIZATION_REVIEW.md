# Audio-Visual Content Technique Operationalization Review

## Reference

- Technique: **T1683.002 — Audio-Visual Content**

Adversaries may create or manipulate audio, image, and video content to support targeting and malicious operations. Adversaries may also use synthetic voice recordings, real-time altered audio or video during live interactions, fabricated profile photos and identity documents, or video content depicting fabricated or impersonated individuals. Content may be produced manually through editing tools, generated using AI-assisted tools, or produced using third-party synthetic services. AI-assisted tools have enabled adversaries to produce synthetic media at scale and generate content that is more difficult to identify as inauthentic. Audio-visual content produced through these methods may be used in support of other techniques, such as Phishing, Spearphishing via Service, Phishing for Information, Internal Spearphishing, Social Engineering, Financial Theft, or Establish Accounts.

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
- T1683.002: https://attack.mitre.org/techniques/T1683/002
- Reviewed: 2026-10-27
