# Generate Content Technique Response Playbook

## Target technique

**T1683 — Generate Content**

- Tactics: resource-development
- Platforms: PRE

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support Social Engineering, fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective. Content development may occur prior to or during an operation. Adversaries may develop or generate content in-house, source it through third parties, or produce it using AI-assisted tools. Adversaries may use AI to research targets, develop pretexts, and better understand the organizations and individuals they intend to target or deceive prior to generating content (i.e., Query Public AI Services); for obtaining access to AI tools used in content generation, see Artificial Intelligence. Content may be leveraged in support of techniques such as Phishing, Phishing for Information, Social Engineering, Financial Theft, or Establish Accounts. Generated or developed content does not include malicious code or scripts (i.e., Develop Capabilities and Artificial Intelligence).

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
- T1683: https://attack.mitre.org/techniques/T1683
- Reviewed: 2026-10-27
