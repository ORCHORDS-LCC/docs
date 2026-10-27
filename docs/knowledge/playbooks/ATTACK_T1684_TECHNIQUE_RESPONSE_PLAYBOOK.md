# Social Engineering Technique Response Playbook

## Target technique

**T1684 — Social Engineering**

- Tactics: stealth
- Platforms: Linux, macOS, Office Suite, SaaS, Windows

Adversaries may use social engineering techniques to influence users to take actions that result in unauthorized access, approval of changes, disclosure of sensitive information, or execution of adversary-supplied instructions (i.e., introduction of malicious payloads or software), while minimizing technical indicators. Adversaries may leverage trust-building methods across multiple channels (e.g., executive, vendor, or help desk scenarios, including AI-enabled voice interactions) to prompt user-authorized actions such as password resets, MFA changes, financial approvals, or the disclosure of sensitive information. Adversaries may also leverage common business communications and workflows such as email, collaboration platforms, voice communications, recruiting processes, help desk interactions, and SaaS consent mechanisms to make malicious requests appear routine and legitimate. Additionally, adversaries have persuaded victims to take actions through references of current events, harnessing relevant themes to the work role or the organizations mission. For example, adversaries may use scare tactics (i.e., threaten repercussions for non-compliance) or otherwise incite victims’ emotions in order to generate a sense of urgency to take action. This technique may include common social engineering patterns such as Phishing and Spearphishing Voice, often supported by convincing and targeted narratives.

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
- T1684: https://attack.mitre.org/techniques/T1684
- Reviewed: 2026-10-27
