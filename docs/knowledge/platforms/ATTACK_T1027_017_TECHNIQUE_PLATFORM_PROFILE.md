# SVG Smuggling Technique Platform Profile

## Reference

- Technique: **T1027.017 — SVG Smuggling**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign SVG files. SVGs, or Scalable Vector Graphics, are vector-based image files constructed using XML. As such, they can legitimately include `<script>` tags that enable adversaries to include malicious JavaScript payloads. However, SVGs may appear less suspicious to users than other types of executable files, as they are often treated as image files. SVG smuggling can take a number of forms. For example, threat actors may include content that: * Assembles malicious payloads * Downloads malicious payloads * Redirects users to malicious websites * Displays interactive content to users, such as fake login forms and download buttons. SVG Smuggling may be used in conjunction with HTML Smuggling where an SVG with a malicious payload is included inside an HTML file. SVGs may also be included in other types of documents, such as PDFs.

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
- T1027.017: https://attack.mitre.org/techniques/T1027/017
- Reviewed: 2026-10-27
