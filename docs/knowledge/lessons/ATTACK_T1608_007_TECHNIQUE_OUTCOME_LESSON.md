# T1608.007 AI Result Poisoning Outcome Lesson

## Authoritative description

- Technique: **T1608.007 — AI Result Poisoning**
- Tactics: resource-development
- Platforms: PRE

Adversaries may manipulate publicly accessible web content to influence generative AI systems or AI-powered search engines into retrieving, citing, or recommending attacker-controlled information. Unlike traditional SEO Poisoning, which primarily attempts to influence the ordering of conventional search results, AI Result Poisoning targets systems that synthesize information from multiple sources and provide a direct answer to the user. Adversaries may create malicious or misleading websites, publish fabricated claims, generate supporting articles, or establish multiple apparently independent sources that reinforce the same information. These sources may then be retrieved by AI systems using web search or retrieval-augmented generation and incorporated into generated responses. Adversaries may use this technique to recommend or link to phishing sites, fraudulent online stores, malicious downloads, impersonation pages, or other attacker-controlled infrastructure. It can also be used to promote misinformation or fabricated claims without requiring access to the underlying AI model, system prompt, or application infrastructure. Because the malicious content can resemble ordinary marketing, editorial, or informational material, traditional prompt injection and malware-focused detections may not identify the activity.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1608.007: https://attack.mitre.org/techniques/T1608/007
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
