# Kali365 Technique Response Playbook

## Target technique

**S9044 — Kali365**

- Platforms: IaaS, macOS, Windows

Kali365 is a Phishing-as-a-Service (PHaaS) kit first observed in April 2026 that generates victim-targeted lures across multiple operating systems to induce users into copying and pasting actor-controlled commands for local execution. Kali365 incorporates on-demand device code generation and mirrors the copy-paste execution tradecraft associated with ClickFix. Operators have used Kali365 to harvest victims' OAuth tokens and session cookies through adversary-in-the-middle (AiTM) interception, enabling account takeover. Kali365 PHaaS was first observed in April 2026. Kali365 has also been affiliated with other branding to include Octopi365 and Freedom365.

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
- S9044: https://attack.mitre.org/software/S9044
- Reviewed: 2026-10-27
