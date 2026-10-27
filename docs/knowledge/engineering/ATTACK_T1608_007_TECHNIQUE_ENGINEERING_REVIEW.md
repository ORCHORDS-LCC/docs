# AI Result Poisoning Technique Engineering Review

## Reference

- Technique: **T1608.007 — AI Result Poisoning**

Adversaries may manipulate publicly accessible web content to influence generative AI systems or AI-powered search engines into retrieving, citing, or recommending attacker-controlled information. Unlike traditional SEO Poisoning, which primarily attempts to influence the ordering of conventional search results, AI Result Poisoning targets systems that synthesize information from multiple sources and provide a direct answer to the user. Adversaries may create malicious or misleading websites, publish fabricated claims, generate supporting articles, or establish multiple apparently independent sources that reinforce the same information. These sources may then be retrieved by AI systems using web search or retrieval-augmented generation and incorporated into generated responses. Adversaries may use this technique to recommend or link to phishing sites, fraudulent online stores, malicious downloads, impersonation pages, or other attacker-controlled infrastructure. It can also be used to promote misinformation or fabricated claims without requiring access to the underlying AI model, system prompt, or application infrastructure. Because the malicious content can resemble ordinary marketing, editorial, or informational material, traditional prompt injection and malware-focused detections may not identify the activity.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1608.007: https://attack.mitre.org/techniques/T1608/007
- Reviewed: 2026-10-27
