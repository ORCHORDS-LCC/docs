# Hide Infrastructure Technique Response Playbook

## Target technique

**T1665 — Hide Infrastructure**

- Tactics: command-and-control
- Platforms: ESXi, Linux, macOS, Network Devices, Windows

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools, masking malicious domains to obfuscate the true destination from both automated scanning tools and security researchers, and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely. C2 networks may include the use of Proxy or VPNs to disguise IP addresses, which can allow adversaries to blend in with normal network traffic and bypass conditional access policies or anti-abuse protections. For example, an adversary may use a virtual private cloud to spoof their IP address to closer align with a victim's IP address ranges. This may also bypass security measures relying on geolocation of the source IP address. Adversaries may also attempt to filter network traffic in order to evade defensive tools in numerous ways, including blocking/redirecting common incident responder or security appliance user agents. Filtering traffic based on IP and geo-fencing may also avoid automated sandboxing or researcher activity (i.e., Virtualization/Sandbox Evasion). Hiding C2 infrastructure may also be supported by Resource Development activities such as Acquire Infrastructure and Compromise Infrastructure. For example, using widely trusted hosting services or domains such as prominent URL shortening providers or marketing services for C2 networks may enable adversaries to present benign content that later redirects victims to malicious web pages or infrastructure once specific conditions are met.

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
- T1665: https://attack.mitre.org/techniques/T1665
- Reviewed: 2026-10-27
