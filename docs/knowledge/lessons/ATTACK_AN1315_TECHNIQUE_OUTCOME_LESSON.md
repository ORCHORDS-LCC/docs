# AN1315 Analytic 1315 Outcome Lesson

## Authoritative description

- Technique: **AN1315 — Analytic 1315**
- Platforms: Linux

Cause→effect chain: (1) User app/browser/archiver logs an open/click or abnormal exit, (2) new executable/script/archive extracted into $HOME/Downloads, /tmp, or ~/.cache, (3) parent app spawns shell/interpreter (bash/sh/python/node/curl/wget) or desktop file, and (4) new outbound connection(s) from the child lineage.

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
- AN1315: https://attack.mitre.org/detectionstrategies/DET0478#AN1315
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
