# Black Basta Technique Response Playbook

## Target technique

**S1070 — Black Basta**

- Platforms: Windows, ESXi

Black Basta is ransomware written in C++ that has been offered within the ransomware-as-a-service (RaaS) model since at least April 2022; there are variants that target Windows and VMWare ESXi servers. Black Basta operations have included the double extortion technique where in addition to demanding ransom for decrypting the files of targeted organizations the cyber actors also threaten to post sensitive information to a leak site if the ransom is not paid. Black Basta affiliates have targeted multiple high-value organizations, with the largest number of victims based in the U.S. Based on similarities in TTPs, leak sites, payment sites, and negotiation tactics, security researchers assess the Black Basta RaaS operators could include current or former members of the Conti group.

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
- S1070: https://attack.mitre.org/software/S1070
- Reviewed: 2026-10-27
