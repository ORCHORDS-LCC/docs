# Analytic 1980 Technique Response Playbook

## Target technique

**AN1980 — Analytic 1980**

- Platforms: PRE

Consider use of services that may aid in the tracking of newly issued certificates and/or certificates in use on sites across the Internet. In some cases it may be possible to pivot on known pieces of certificate information to uncover other adversary infrastructure. Some server-side components of adversary tools may have default values set for SSL/TLS certificates. Monitor for logged network traffic in response to a scan showing both protocol header and body values that may buy and/or steal SSL/TLS certificates that can be used during targeting. Detection efforts may be focused on related behaviors, such as Web Protocols, Asymmetric Cryptography, and/or Install Root Certificate.

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
- AN1980: https://attack.mitre.org/detectionstrategies/DET0848#AN1980
- Reviewed: 2026-10-27
