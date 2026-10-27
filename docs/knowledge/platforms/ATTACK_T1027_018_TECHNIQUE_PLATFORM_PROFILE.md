# Invisible Unicode Technique Platform Profile

## Reference

- Technique: **T1027.018 — Invisible Unicode**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may abuse invisible or non-printing Unicode characters to conceal malicious content within files, scripts, or text. By inserting characters that do not visibly render, adversaries may hide data, alter how content is interpreted, or make malicious code appear as benign text or whitespace. Adversaries may encode these malicious payloads, using binary, Base64, or custom schemes, to be reconstructed at runtime through scripting features such as JavaScript Proxy traps, `eval()`, or other dynamic execution methods. This technique enables adversaries to evade visual inspection and basic static analysis by hiding malicious encoded content in innocuous text. Unicode is a standardized character encoding model that assigns a unique numerical value, known as a code point, to every character across writing systems, enabling consistent text representation across platforms, applications, and languages. Code points are represented as `U+` followed by a hexadecimal value and may be encoded using formats such as `UTF-8` or `UTF-16`. Adversaries may abuse the valid code points in Unicode that are not visibly rendered but still take up bytes, such as zero-width spaces, variation selectors, or bidirectional formatting controls, to conceal malicious payloads. Adversaries may additionally exploit Private Use Area (PUA) characters, a range of code points reserved for custom assignment. PUA characters that are not defined by a font or application are typically rendered blank. Unicode characters may also be leveraged in support of other techniques such as Phishing, Right-to-Left Override, or User Execution. For example, some adversaries may embed artificial intelligence (AI) prompt injections using invisible Unicode characters in emails or documents that appear benign when processed by AI systems.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1027.018: https://attack.mitre.org/techniques/T1027/018
- Reviewed: 2026-10-27
