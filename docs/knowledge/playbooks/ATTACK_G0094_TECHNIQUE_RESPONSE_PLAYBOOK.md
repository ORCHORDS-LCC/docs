# Kimsuky Technique Response Playbook

## Target technique

**G0094 — Kimsuky**


Kimsuky is a Democratic People's Republic of Korea (DPRK)-based cyber espionage group that has been active since at least 2012. The group initially targeted South Korean government agencies, think tanks, and subject-matter experts in various fields. Its operations expanded to include the United Nations and organizations in the government, education, business services, and manufacturing sectors across the United States, Japan, Russia, and Europe. Kimsuky has focused collection on foreign policy and national security issues tied to the Korean Peninsula, nuclear policy, and sanctions. Kimsuky operations have overlapped with those of other North Korean state-sponsored cyber espionage actors as a result of ad hoc collaborations or other limited resource sharing. Kimsuky was assessed to be responsible for the 2014 Korea Hydro & Nuclear Power Co. compromise; other notable campaigns include Operation STOLEN PENCIL (2018), Operation Kabar Cobra (2019), and Operation Smoke Screen (2019). In 2023, Kimsuky was observed using commercial large language models (LLMs) to assist with vulnerability research, scripting, social engineering and reconnaissance. DPRK threat actor cluster boundaries overlap in open source reporting, with some security researchers consolidating all attributed North Korean state-sponsored cyber activity under Lazarus Group, rather than tracking operationally distinct subgroups.

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
- G0094: https://attack.mitre.org/groups/G0094
- Reviewed: 2026-10-27
