# Uroburos Technique Response Playbook

## Target technique

**S0022 — Uroburos**

- Platforms: Linux, Windows, macOS

Uroburos is a sophisticated cyber espionage tool written in C that has been used by units within Russia's Federal Security Service (FSB) associated with the Turla toolset to collect intelligence on sensitive targets worldwide. Uroburos has several variants and has undergone nearly constant upgrade since its initial development in 2003 to keep it viable after public disclosures. Uroburos is typically deployed to external-facing nodes on a targeted network and has the ability to leverage additional tools and TTPs to further exploit an internal network. Uroburos has interoperable implants for Windows, Linux, and macOS, employs a high level of stealth in communications and architecture, and can easily incorporate new or replacement components.

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
- S0022: https://attack.mitre.org/software/S0022
- Reviewed: 2026-10-27
