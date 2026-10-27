# AI Result Poisoning Technique Platform Profile

## Reference

- Technique: **T1608.007 — AI Result Poisoning**
- Platforms named in the source: PRE

Adversaries may manipulate publicly accessible web content to influence generative AI systems or AI-powered search engines into retrieving, citing, or recommending attacker-controlled information. Unlike traditional SEO Poisoning, which primarily attempts to influence the ordering of conventional search results, AI Result Poisoning targets systems that synthesize information from multiple sources and provide a direct answer to the user. Adversaries may create malicious or misleading websites, publish fabricated claims, generate supporting articles, or establish multiple apparently independent sources that reinforce the same information. These sources may then be retrieved by AI systems using web search or retrieval-augmented generation and incorporated into generated responses. Adversaries may use this technique to recommend or link to phishing sites, fraudulent online stores, malicious downloads, impersonation pages, or other attacker-controlled infrastructure. It can also be used to promote misinformation or fabricated claims without requiring access to the underlying AI model, system prompt, or application infrastructure. Because the malicious content can resemble ordinary marketing, editorial, or informational material, traditional prompt injection and malware-focused detections may not identify the activity.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1608.007: https://attack.mitre.org/techniques/T1608/007
- Reviewed: 2026-10-27
