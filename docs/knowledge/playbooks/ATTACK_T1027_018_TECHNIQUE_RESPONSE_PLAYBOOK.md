# Invisible Unicode Technique Response Playbook

## Target technique

**T1027.018 — Invisible Unicode**

- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may abuse invisible or non-printing Unicode characters to conceal malicious content within files, scripts, or text. By inserting characters that do not visibly render, adversaries may hide data, alter how content is interpreted, or make malicious code appear as benign text or whitespace. Adversaries may encode these malicious payloads, using binary, Base64, or custom schemes, to be reconstructed at runtime through scripting features such as JavaScript Proxy traps, `eval()`, or other dynamic execution methods. This technique enables adversaries to evade visual inspection and basic static analysis by hiding malicious encoded content in innocuous text. Unicode is a standardized character encoding model that assigns a unique numerical value, known as a code point, to every character across writing systems, enabling consistent text representation across platforms, applications, and languages. Code points are represented as `U+` followed by a hexadecimal value and may be encoded using formats such as `UTF-8` or `UTF-16`. Adversaries may abuse the valid code points in Unicode that are not visibly rendered but still take up bytes, such as zero-width spaces, variation selectors, or bidirectional formatting controls, to conceal malicious payloads. Adversaries may additionally exploit Private Use Area (PUA) characters, a range of code points reserved for custom assignment. PUA characters that are not defined by a font or application are typically rendered blank. Unicode characters may also be leveraged in support of other techniques such as Phishing, Right-to-Left Override, or User Execution. For example, some adversaries may embed artificial intelligence (AI) prompt injections using invisible Unicode characters in emails or documents that appear benign when processed by AI systems.

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
- T1027.018: https://attack.mitre.org/techniques/T1027/018
- Reviewed: 2026-10-27
