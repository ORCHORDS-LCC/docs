# T1027.017 SVG Smuggling Outcome Lesson

## Authoritative description

- Technique: **T1027.017 — SVG Smuggling**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign SVG files. SVGs, or Scalable Vector Graphics, are vector-based image files constructed using XML. As such, they can legitimately include `<script>` tags that enable adversaries to include malicious JavaScript payloads. However, SVGs may appear less suspicious to users than other types of executable files, as they are often treated as image files. SVG smuggling can take a number of forms. For example, threat actors may include content that: * Assembles malicious payloads * Downloads malicious payloads * Redirects users to malicious websites * Displays interactive content to users, such as fake login forms and download buttons. SVG Smuggling may be used in conjunction with HTML Smuggling where an SVG with a malicious payload is included inside an HTML file. SVGs may also be included in other types of documents, such as PDFs.

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
- T1027.017: https://attack.mitre.org/techniques/T1027/017
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
