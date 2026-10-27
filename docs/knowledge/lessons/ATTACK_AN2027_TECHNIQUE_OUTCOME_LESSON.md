# AN2027 Analytic 2027 Outcome Lesson

## Authoritative description

- Technique: **AN2027 — Analytic 2027**
- Platforms: PRE

Monitor for contextual data about an Internet-facing resource gathered from a scan, such as running services or ports that may buy, lease, or rent infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Once adversaries have provisioned infrastructure (ex: a server for use in command and control), internet scans may help proactively discover adversary acquired infrastructure. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for queried domain name system (DNS) registry data that may buy, lease, or rent infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for logged domain name system (DNS) data that may buy, lease, or rent infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Consider use of services that may aid in tracking of newly acquired infrastructure, such as WHOIS databases for domain registration information. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN2027: https://attack.mitre.org/detectionstrategies/DET0895#AN2027
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
