# AN0647 Analytic 0647 Outcome Lesson

## Authoritative description

- Technique: **AN0647 — Analytic 0647**
- Platforms: Network Devices

Defenders may observe adversary attempts to collect or export full device configurations by detecting unusual SNMP queries, Smart Install (SMI) activity, or CLI/API commands that request running or startup configuration dumps. Correlated behaviors include high-volume read requests for sensitive OIDs, repeated use of 'show running-config' or equivalent commands from untrusted IPs, or unexpected TFTP/SCP/FTP transfers containing configuration files. These behaviors often appear in sequence: anomalous authentication or privilege escalation, followed by bulk configuration retrieval and outbound transfer.

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
- AN0647: https://attack.mitre.org/detectionstrategies/DET0233#AN0647
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
