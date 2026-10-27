# SVG Smuggling Technique Engineering Review

## Reference

- Technique: **T1027.017 — SVG Smuggling**

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign SVG files. SVGs, or Scalable Vector Graphics, are vector-based image files constructed using XML. As such, they can legitimately include `` tags that enable adversaries to include malicious JavaScript payloads. However, SVGs may appear less suspicious to users than other types of executable files, as they are often treated as image files. SVG smuggling can take a number of forms. For example, threat actors may include content that: * Assembles malicious payloads * Downloads malicious payloads * Redirects users to malicious websites * Displays interactive content to users, such as fake login forms and download buttons. SVG Smuggling may be used in conjunction with HTML Smuggling where an SVG with a malicious payload is included inside an HTML file. SVGs may also be included in other types of documents, such as PDFs.

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
- T1027.017: https://attack.mitre.org/techniques/T1027/017
- Reviewed: 2026-10-27
