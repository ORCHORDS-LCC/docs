# T1490 Inhibit System Recovery Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1490 — Inhibit System Recovery Mitigation**

Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. Identify potentially malicious software and audit and/or block it by using whitelisting tools, like AppLocker, or Software Restriction Policies where appropriate.

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
- T1490: https://attack.mitre.org/mitigations/T1490
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
