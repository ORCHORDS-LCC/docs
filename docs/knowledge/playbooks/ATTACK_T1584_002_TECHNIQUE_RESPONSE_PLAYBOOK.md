# DNS Server Technique Response Playbook

## Target technique

**T1584.002 — DNS Server**

- Tactics: resource-development
- Platforms: PRE

Adversaries may compromise third-party DNS servers that can be used during targeting. During post-compromise activity, adversaries may utilize DNS traffic for various tasks, including for Command and Control (ex: Application Layer Protocol). Instead of setting up their own DNS servers, adversaries may compromise third-party DNS servers in support of operations. By compromising DNS servers, adversaries can alter DNS records. Such control can allow for redirection of an organization's traffic, facilitating Collection and Credential Access efforts for the adversary. Additionally, adversaries may leverage such control in conjunction with Digital Certificates to redirect traffic to adversary-controlled infrastructure, mimicking normal trusted network communications. Alternatively, they may be able to prove ownership of a domain to a SaaS service in order to assert control of the service or create a new administrative Cloud Account. Adversaries may also be able to silently create subdomains pointed at malicious servers without tipping off the actual owner of the DNS server.

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
- T1584.002: https://attack.mitre.org/techniques/T1584/002
- Reviewed: 2026-10-27
