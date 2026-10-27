# Invisible Unicode Technique Engineering Review

## Reference

- Technique: **T1027.018 — Invisible Unicode**

Adversaries may abuse invisible or non-printing Unicode characters to conceal malicious content within files, scripts, or text. By inserting characters that do not visibly render, adversaries may hide data, alter how content is interpreted, or make malicious code appear as benign text or whitespace. Adversaries may encode these malicious payloads, using binary, Base64, or custom schemes, to be reconstructed at runtime through scripting features such as JavaScript Proxy traps, `eval()`, or other dynamic execution methods. This technique enables adversaries to evade visual inspection and basic static analysis by hiding malicious encoded content in innocuous text. Unicode is a standardized character encoding model that assigns a unique numerical value, known as a code point, to every character across writing systems, enabling consistent text representation across platforms, applications, and languages. Code points are represented as `U+` followed by a hexadecimal value and may be encoded using formats such as `UTF-8` or `UTF-16`. Adversaries may abuse the valid code points in Unicode that are not visibly rendered but still take up bytes, such as zero-width spaces, variation selectors, or bidirectional formatting controls, to conceal malicious payloads. Adversaries may additionally exploit Private Use Area (PUA) characters, a range of code points reserved for custom assignment. PUA characters that are not defined by a font or application are typically rendered blank. Unicode characters may also be leveraged in support of other techniques such as Phishing, Right-to-Left Override, or User Execution. For example, some adversaries may embed artificial intelligence (AI) prompt injections using invisible Unicode characters in emails or documents that appear benign when processed by AI systems.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1027.018: https://attack.mitre.org/techniques/T1027/018
- Reviewed: 2026-10-27
