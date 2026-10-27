# T1567.003 Exfiltration to Text Storage Sites Outcome Lesson

## Authoritative description

- Technique: **T1567.003 — Exfiltration to Text Storage Sites**
- Tactics: exfiltration
- Platforms: Linux, macOS, Windows, ESXi

Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel. Text storage sites, such as pastebin[.]com, are commonly used by developers to share code and other information. Text storage sites are often used to host malicious code for C2 communication (e.g., Stage Capabilities), but adversaries may also use these sites to exfiltrate collected data. Furthermore, paid features and encryption options may allow adversaries to conceal and store data more securely. **Note:** This is distinct from Exfiltration to Code Repository, which highlight access to code repositories via APIs.

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
- T1567.003: https://attack.mitre.org/techniques/T1567/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
