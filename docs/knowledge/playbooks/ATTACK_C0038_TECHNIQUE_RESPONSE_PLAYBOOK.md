# HomeLand Justice Technique Response Playbook

## Target technique

**C0038 — HomeLand Justice**


HomeLand Justice was a disruptive cyber campaign conducted by Iranian state-affiliated actors against Albanian government networks in July and September 2022. The activity combined ransomware, wiper malware, and data leak operations. Initial access for HomeLand Justice was established as early as May 2021, and threat actors moved laterally, exfiltrated sensitive information, and maintained persistence for approximately 14 months prior to the destructive phase of the operation. Responsibility was claimed by the "HomeLand Justice" front, which framed the campaign as retaliation against the Mujahedeen-e Khalq (MEK), an Iranian opposition group with a presence in Albania. Multiple Iran-nexus groups are assessed to have participated in the campaign, including HEXANE who probed victim infrastructure. A second wave of attacks was launched in September 2022 using similar tactics following public attribution of the previous activity to Iran and the severing of diplomatic ties between Iran and Albania.

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
- C0038: https://attack.mitre.org/campaigns/C0038
- Reviewed: 2026-10-27
