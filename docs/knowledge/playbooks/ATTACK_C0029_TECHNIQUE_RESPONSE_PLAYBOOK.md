# Cutting Edge Technique Response Playbook

## Target technique

**C0029 — Cutting Edge**


Cutting Edge was a campaign conducted by suspected China-nexus espionage actors, variously identified as UNC5221/UTA0178 and UNC5325, that began as early as December 2023 with the exploitation of zero-day vulnerabilities in Ivanti Connect Secure (previously Pulse Secure) VPN appliances. Cutting Edge targeted the U.S. defense industrial base and multiple sectors globally including telecommunications, financial, aerospace, and technology. Cutting Edge featured the use of defense evasion and living-off-the-land (LoTL) techniques along with the deployment of web shells and other custom malware.

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
- C0029: https://attack.mitre.org/campaigns/C0029
- Reviewed: 2026-10-27
