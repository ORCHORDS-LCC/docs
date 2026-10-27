# AI Result Poisoning Technique Operationalization Review

## Reference

- Technique: **T1608.007 — AI Result Poisoning**

Adversaries may manipulate publicly accessible web content to influence generative AI systems or AI-powered search engines into retrieving, citing, or recommending attacker-controlled information. Unlike traditional SEO Poisoning, which primarily attempts to influence the ordering of conventional search results, AI Result Poisoning targets systems that synthesize information from multiple sources and provide a direct answer to the user. Adversaries may create malicious or misleading websites, publish fabricated claims, generate supporting articles, or establish multiple apparently independent sources that reinforce the same information. These sources may then be retrieved by AI systems using web search or retrieval-augmented generation and incorporated into generated responses. Adversaries may use this technique to recommend or link to phishing sites, fraudulent online stores, malicious downloads, impersonation pages, or other attacker-controlled infrastructure. It can also be used to promote misinformation or fabricated claims without requiring access to the underlying AI model, system prompt, or application infrastructure. Because the malicious content can resemble ordinary marketing, editorial, or informational material, traditional prompt injection and malware-focused detections may not identify the activity.

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
- T1608.007: https://attack.mitre.org/techniques/T1608/007
- Reviewed: 2026-10-27
