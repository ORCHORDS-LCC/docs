# AN1196 Analytic 1196 Outcome Lesson

## Authoritative description

- Technique: **AN1196 — Analytic 1196**
- Platforms: Linux

Abuse of bind mounts to obscure process directories. Defender perspective: detecting anomalous mount operations where a process’s /proc entry is remapped to another directory, often hiding malicious activity from native utilities (ps, top). Behavior chain includes: (1) execution of `mount` with `-o bind` or `-B` flags, (2) modification of /proc entries inconsistent with expected process lineage, and (3) subsequent anomalous activity from processes whose metadata no longer matches execution context.

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
- AN1196: https://attack.mitre.org/detectionstrategies/DET0428#AN1196
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
