# AN2007 Analytic 2007 Outcome Lesson

## Authoritative description

- Technique: **AN2007 — Analytic 2007**
- Platforms: PRE

Consider analyzing code signing certificates for features that may be associated with the adversary and/or their developers, such as the thumbprint, algorithm used, validity period, common name, and certificate authority. Malware repositories can also be used to identify additional samples associated with the adversary and identify patterns an adversary has used in procuring code signing certificates. Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related follow-on behavior, such as Code Signing or Install Root Certificate.

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
- AN2007: https://attack.mitre.org/detectionstrategies/DET0875#AN2007
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
