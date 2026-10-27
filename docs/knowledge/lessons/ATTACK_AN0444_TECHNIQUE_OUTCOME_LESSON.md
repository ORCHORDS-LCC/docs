# AN0444 Analytic 0444 Outcome Lesson

## Authoritative description

- Technique: **AN0444 — Analytic 0444**
- Platforms: Windows

Detects Kerberoasting attempts by monitoring for anomalous Kerberos TGS requests (Event ID 4769) with RC4 encryption (etype 0x17), accounts requesting an unusual number of service tickets in a short period, or service accounts targeted outside normal usage baselines. Also correlates suspicious process activity (e.g., Mimikatz invoking LSASS access) with Kerberos ticket anomalies.

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
- AN0444: https://attack.mitre.org/detectionstrategies/DET0157#AN0444
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
