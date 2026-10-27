# Written Content Technique Platform Profile

## Reference

- Technique: **T1683.001 — Written Content**
- Platforms named in the source: PRE

Adversaries may create or tailor written materials to support targeting and malicious operations. Content may include phishing lures, fraudulent financial communications, fabricated job postings, fabricated employment credentials and documentation, decoy documents, social media persona content, and supporting narratives used to sustain fabricated personas over time. Content may be authored manually, commissioned through third parties, or produced using AI-assisted tools. Written materials may impersonate legitimate government correspondence, diplomatic communications, or internal organizational documents to support targeting efforts. AI-assisted tools may also be used to tailor content to specific targets, industries, or regions. For example, adversaries may leverage AI to translate content into a target's native language or mimic the communication style of trusted senders. Written content produced through these methods may be used in support of other techniques, such as Phishing, Spearphishing via Service, Phishing for Information, Internal Spearphishing, Social Engineering, Financial Theft, or Establish Accounts. Written content does not include malicious code or scripts; for development of malicious code and scripts, see Develop Capabilities.

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
- T1683.001: https://attack.mitre.org/techniques/T1683/001
- Reviewed: 2026-10-27
