# Query Public AI Services Technique Response Playbook

## Target technique

**T1682 — Query Public AI Services**

- Tactics: reconnaissance
- Platforms: PRE

Adversaries may query publicly accessible artificial intelligence (AI) services, such as large language models (LLMs), to support targeting and operations. In addition to searching websites or databases directly (i.e., Search Open Websites/Domains), adversaries may use AI services to synthesize, aggregate, and analyze publicly available information at scale. This may include identifying individuals or organizations to target, researching organizational structures and personnel, identifying technologies used by target organizations, researching business relationships to develop plausible pretexts for Social Engineering approaches, identifying contact information for use in Phishing or Phishing for Information, or gathering derogatory or sensitive information about individuals that may be used for extortion or coercion. Information gathered through AI services may be leveraged for other behaviors, such as establishing operational resources (i.e., Generate Content or Establish Accounts. For obtaining access to AI tools and services, see Artificial Intelligence.

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
- T1682: https://attack.mitre.org/techniques/T1682
- Reviewed: 2026-10-27
