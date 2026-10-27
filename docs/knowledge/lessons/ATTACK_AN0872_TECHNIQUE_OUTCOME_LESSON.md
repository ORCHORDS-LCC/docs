# AN0872 Analytic 0872 Outcome Lesson

## Authoritative description

- Technique: **AN0872 — Analytic 0872**
- Platforms: Windows

Detection of browser-based or email client-driven file creation (often from temp directories) following navigation to or execution of HTML files containing JavaScript Blob APIs or base64 Data URLs, with follow-on execution of the dropped payload. Leveraging Sysmon EventID 15 to inspect Zone.Identifier ADS for HostUrl/ReferrerUrl indicators (e.g., HostUrl=about:internet). Optional: absence of a large HTTP download record for the same URL/client in proxy logs (suggests local assembly).

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
- AN0872: https://attack.mitre.org/detectionstrategies/DET0313#AN0872
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
