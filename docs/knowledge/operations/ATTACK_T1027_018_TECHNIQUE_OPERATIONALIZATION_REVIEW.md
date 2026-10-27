# Invisible Unicode Technique Operationalization Review

## Reference

- Technique: **T1027.018 — Invisible Unicode**

Adversaries may abuse invisible or non-printing Unicode characters to conceal malicious content within files, scripts, or text. By inserting characters that do not visibly render, adversaries may hide data, alter how content is interpreted, or make malicious code appear as benign text or whitespace. Adversaries may encode these malicious payloads, using binary, Base64, or custom schemes, to be reconstructed at runtime through scripting features such as JavaScript Proxy traps, `eval()`, or other dynamic execution methods. This technique enables adversaries to evade visual inspection and basic static analysis by hiding malicious encoded content in innocuous text. Unicode is a standardized character encoding model that assigns a unique numerical value, known as a code point, to every character across writing systems, enabling consistent text representation across platforms, applications, and languages. Code points are represented as `U+` followed by a hexadecimal value and may be encoded using formats such as `UTF-8` or `UTF-16`. Adversaries may abuse the valid code points in Unicode that are not visibly rendered but still take up bytes, such as zero-width spaces, variation selectors, or bidirectional formatting controls, to conceal malicious payloads. Adversaries may additionally exploit Private Use Area (PUA) characters, a range of code points reserved for custom assignment. PUA characters that are not defined by a font or application are typically rendered blank. Unicode characters may also be leveraged in support of other techniques such as Phishing, Right-to-Left Override, or User Execution. For example, some adversaries may embed artificial intelligence (AI) prompt injections using invisible Unicode characters in emails or documents that appear benign when processed by AI systems.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1027.018: https://attack.mitre.org/techniques/T1027/018
- Reviewed: 2026-10-27
