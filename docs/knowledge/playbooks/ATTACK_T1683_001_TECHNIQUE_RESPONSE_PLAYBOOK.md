# Written Content Technique Response Playbook

## Target technique

**T1683.001 — Written Content**

- Tactics: resource-development
- Platforms: PRE

Adversaries may create or tailor written materials to support targeting and malicious operations. Content may include phishing lures, fraudulent financial communications, fabricated job postings, fabricated employment credentials and documentation, decoy documents, social media persona content, and supporting narratives used to sustain fabricated personas over time. Content may be authored manually, commissioned through third parties, or produced using AI-assisted tools. Written materials may impersonate legitimate government correspondence, diplomatic communications, or internal organizational documents to support targeting efforts. AI-assisted tools may also be used to tailor content to specific targets, industries, or regions. For example, adversaries may leverage AI to translate content into a target's native language or mimic the communication style of trusted senders. Written content produced through these methods may be used in support of other techniques, such as Phishing, Spearphishing via Service, Phishing for Information, Internal Spearphishing, Social Engineering, Financial Theft, or Establish Accounts. Written content does not include malicious code or scripts; for development of malicious code and scripts, see Develop Capabilities.

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
- T1683.001: https://attack.mitre.org/techniques/T1683/001
- Reviewed: 2026-10-27
