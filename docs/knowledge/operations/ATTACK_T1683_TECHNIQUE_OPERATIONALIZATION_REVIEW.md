# Generate Content Technique Operationalization Review

## Reference

- Technique: **T1683 — Generate Content**

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support Social Engineering, fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective. Content development may occur prior to or during an operation. Adversaries may develop or generate content in-house, source it through third parties, or produce it using AI-assisted tools. Adversaries may use AI to research targets, develop pretexts, and better understand the organizations and individuals they intend to target or deceive prior to generating content (i.e., Query Public AI Services); for obtaining access to AI tools used in content generation, see Artificial Intelligence. Content may be leveraged in support of techniques such as Phishing, Phishing for Information, Social Engineering, Financial Theft, or Establish Accounts. Generated or developed content does not include malicious code or scripts (i.e., Develop Capabilities and Artificial Intelligence).

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
- T1683: https://attack.mitre.org/techniques/T1683
- Reviewed: 2026-10-27
