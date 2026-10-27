# T1027.018 Invisible Unicode Outcome Lesson

## Authoritative description

- Technique: **T1027.018 — Invisible Unicode**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may abuse invisible or non-printing Unicode characters to conceal malicious content within files, scripts, or text. By inserting characters that do not visibly render, adversaries may hide data, alter how content is interpreted, or make malicious code appear as benign text or whitespace. Adversaries may encode these malicious payloads, using binary, Base64, or custom schemes, to be reconstructed at runtime through scripting features such as JavaScript Proxy traps, `eval()`, or other dynamic execution methods. This technique enables adversaries to evade visual inspection and basic static analysis by hiding malicious encoded content in innocuous text. Unicode is a standardized character encoding model that assigns a unique numerical value, known as a code point, to every character across writing systems, enabling consistent text representation across platforms, applications, and languages. Code points are represented as `U+` followed by a hexadecimal value and may be encoded using formats such as `UTF-8` or `UTF-16`. Adversaries may abuse the valid code points in Unicode that are not visibly rendered but still take up bytes, such as zero-width spaces, variation selectors, or bidirectional formatting controls, to conceal malicious payloads. Adversaries may additionally exploit Private Use Area (PUA) characters, a range of code points reserved for custom assignment. PUA characters that are not defined by a font or application are typically rendered blank. Unicode characters may also be leveraged in support of other techniques such as Phishing, Right-to-Left Override, or User Execution. For example, some adversaries may embed artificial intelligence (AI) prompt injections using invisible Unicode characters in emails or documents that appear benign when processed by AI systems.

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
- T1027.018: https://attack.mitre.org/techniques/T1027/018
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
