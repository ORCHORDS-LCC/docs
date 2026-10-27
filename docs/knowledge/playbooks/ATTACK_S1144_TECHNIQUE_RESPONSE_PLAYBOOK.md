# FRP Technique Response Playbook

## Target technique

**S1144 — FRP**

- Platforms: Linux, macOS, Windows

FRP, which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. FRP can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.

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
- S1144: https://attack.mitre.org/software/S1144
- Reviewed: 2026-10-27
