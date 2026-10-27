# Artificial Intelligence Technique Operationalization Review

## Reference

- Technique: **T1588.007 — Artificial Intelligence**

Adversaries may obtain access to generative artificial intelligence (AI) tools, such as large language models (LLMs), to aid various techniques during targeting. These tools may be used to inform, bolster, and enable a variety of malicious tasks, including creating scripts, assisting social engineering, developing payloads, and to Query Public AI Services in support of Reconnaissance. For example, by utilizing a publicly available LLM an adversary is essentially outsourcing or automating certain tasks to the tool. Using AI, the adversary may draft and Generate Content in a variety of written languages to be used in Phishing/Phishing for Information campaigns. The same publicly available tool may further enable vulnerability or other offensive research supporting Develop Capabilities. AI tools may also automate technical tasks by generating, refining, or otherwise enhancing (e.g., Obfuscated Files or Information) malicious scripts and payloads. Finally, AI-generated text, images, audio, and video may be used for fraud, Impersonation, and other malicious activities.

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
- T1588.007: https://attack.mitre.org/techniques/T1588/007
- Reviewed: 2026-10-27
