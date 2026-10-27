# AI Result Poisoning Technique Response Playbook

## Target technique

**T1608.007 — AI Result Poisoning**

- Tactics: resource-development
- Platforms: PRE

Adversaries may manipulate publicly accessible web content to influence generative AI systems or AI-powered search engines into retrieving, citing, or recommending attacker-controlled information. Unlike traditional SEO Poisoning, which primarily attempts to influence the ordering of conventional search results, AI Result Poisoning targets systems that synthesize information from multiple sources and provide a direct answer to the user. Adversaries may create malicious or misleading websites, publish fabricated claims, generate supporting articles, or establish multiple apparently independent sources that reinforce the same information. These sources may then be retrieved by AI systems using web search or retrieval-augmented generation and incorporated into generated responses. Adversaries may use this technique to recommend or link to phishing sites, fraudulent online stores, malicious downloads, impersonation pages, or other attacker-controlled infrastructure. It can also be used to promote misinformation or fabricated claims without requiring access to the underlying AI model, system prompt, or application infrastructure. Because the malicious content can resemble ordinary marketing, editorial, or informational material, traditional prompt injection and malware-focused detections may not identify the activity.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1608.007: https://attack.mitre.org/techniques/T1608/007
- Reviewed: 2026-10-27
