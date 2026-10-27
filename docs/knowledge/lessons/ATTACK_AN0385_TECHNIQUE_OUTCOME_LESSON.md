# AN0385 Analytic 0385 Outcome Lesson

## Authoritative description

- Technique: **AN0385 — Analytic 0385**
- Platforms: Linux

Processes invoking destructive commands (dd, shred, wipe) with raw device targets (e.g., /dev/sda, /dev/nvme0n1). Detect direct writes to disk partitions and abnormal superblock or bootloader modifications. Correlate shell execution with subsequent block device I/O.

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
- AN0385: https://attack.mitre.org/detectionstrategies/DET0137#AN0385
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
