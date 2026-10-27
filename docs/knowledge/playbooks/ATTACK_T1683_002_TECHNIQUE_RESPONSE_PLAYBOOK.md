# Audio-Visual Content Technique Response Playbook

## Target technique

**T1683.002 — Audio-Visual Content**

- Tactics: resource-development
- Platforms: PRE

Adversaries may create or manipulate audio, image, and video content to support targeting and malicious operations. Adversaries may also use synthetic voice recordings, real-time altered audio or video during live interactions, fabricated profile photos and identity documents, or video content depicting fabricated or impersonated individuals. Content may be produced manually through editing tools, generated using AI-assisted tools, or produced using third-party synthetic services. AI-assisted tools have enabled adversaries to produce synthetic media at scale and generate content that is more difficult to identify as inauthentic. Audio-visual content produced through these methods may be used in support of other techniques, such as Phishing, Spearphishing via Service, Phishing for Information, Internal Spearphishing, Social Engineering, Financial Theft, or Establish Accounts.

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
- T1683.002: https://attack.mitre.org/techniques/T1683/002
- Reviewed: 2026-10-27
