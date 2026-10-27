# AN0646 Analytic 0646 Outcome Lesson

## Authoritative description

- Technique: **AN0646 — Analytic 0646**
- Platforms: ESXi

Detects anomalous usage of ESXi Guest Operations APIs such as StartProgramInGuest, ListProcessesInGuest, ListFileInGuest, or InitiateFileTransferFromGuest. Defender perspective focuses on unusual frequency of guest API calls, invocation from unexpected management accounts, or execution outside of business hours. These correlated signals indicate adversarial abuse of ESXi administrative services to run commands on guest VMs.

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
- AN0646: https://attack.mitre.org/detectionstrategies/DET0232#AN0646
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
