# AN1203 Analytic 1203 Outcome Lesson

## Authoritative description

- Technique: **AN1203 — Analytic 1203**
- Platforms: Linux

Detects spoofed emails by analyzing mail server logs (e.g., Postfix, Sendmail) for mismatched header fields, failed SPF/DKIM checks, and anomalies in SMTP proxy logs. Defender observes discrepancies between sending domain, return-path domain, and message metadata.

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
- AN1203: https://attack.mitre.org/detectionstrategies/DET0431#AN1203
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
