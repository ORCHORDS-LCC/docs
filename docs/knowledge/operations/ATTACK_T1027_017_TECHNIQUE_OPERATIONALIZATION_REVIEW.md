# SVG Smuggling Technique Operationalization Review

## Reference

- Technique: **T1027.017 — SVG Smuggling**

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign SVG files. SVGs, or Scalable Vector Graphics, are vector-based image files constructed using XML. As such, they can legitimately include `<script>` tags that enable adversaries to include malicious JavaScript payloads. However, SVGs may appear less suspicious to users than other types of executable files, as they are often treated as image files. SVG smuggling can take a number of forms. For example, threat actors may include content that: * Assembles malicious payloads * Downloads malicious payloads * Redirects users to malicious websites * Displays interactive content to users, such as fake login forms and download buttons. SVG Smuggling may be used in conjunction with HTML Smuggling where an SVG with a malicious payload is included inside an HTML file. SVGs may also be included in other types of documents, such as PDFs.

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
- T1027.017: https://attack.mitre.org/techniques/T1027/017
- Reviewed: 2026-10-27
