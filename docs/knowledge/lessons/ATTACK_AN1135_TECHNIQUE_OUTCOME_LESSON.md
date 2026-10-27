# AN1135 Analytic 1135 Outcome Lesson

## Authoritative description

- Technique: **AN1135 — Analytic 1135**
- Platforms: Linux

Abuse of extended attributes (xattrs) to embed hidden payloads into legitimate files. Defender perspective: detect anomalous use of setfattr or getfattr commands, or direct syscalls (setxattr, getxattr) where attributes are unusually large or contain encoded data. Behavior chain includes: (1) execution of setfattr with suspicious namespaces (user., trusted.), (2) file metadata modification inconsistent with file size/hash, and (3) subsequent process execution reading attributes followed by decoding activity.

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
- AN1135: https://attack.mitre.org/detectionstrategies/DET0406#AN1135
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
