# AN1144 Analytic 1144 Outcome Lesson

## Authoritative description

- Technique: **AN1144 — Analytic 1144**
- Platforms: Windows

Detects anomalous NTLM LogonType 3 authentications that occur without accompanying domain logon events, especially from lateral systems or involving built-in administrative tools. Monitors for mismatches between source user context and system being accessed. Correlates LogonSession creation, NTLM authentications, and process/service initiation to identify suspicious use of stolen password hashes for remote access or service logon without password entry. Detects overpass-the-hash by combining Kerberos ticket issuance with NTLM-based lateral movement.

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
- AN1144: https://attack.mitre.org/detectionstrategies/DET0409#AN1144
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
