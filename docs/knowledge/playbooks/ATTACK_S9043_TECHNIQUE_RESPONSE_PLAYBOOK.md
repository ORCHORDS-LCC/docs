# Mini Shai-Hulud Technique Response Playbook

## Target technique

**S9043 — Mini Shai-Hulud**

- Platforms: Containers, IaaS, Linux, macOS, SaaS, Windows

Mini Shai-Hulud is a credential stealer and self-replicating supply chain worm, derived from Shai-Hulud, that has been used by TeamPCP to target Continuous Integration and Continuous Delivery/Deployment (CI/CD) workflows since at least 2026. Mini Shai-Hulud can compromise credentials across multiple cloud, container, and AI configuration file paths and can use stolen npm and GitHub OIDC tokens to spread to other packages maintained by the compromised user. Mini Shai-Hulud also has a targeted wiper component and has used multiple C2 and data exfiltration mechanisms.

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
- S9043: https://attack.mitre.org/software/S9043
- Reviewed: 2026-10-27
