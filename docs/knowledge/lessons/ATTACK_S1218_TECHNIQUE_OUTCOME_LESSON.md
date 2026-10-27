# S1218 VIRTUALPIE Outcome Lesson

## Authoritative description

- Technique: **S1218 — VIRTUALPIE**
- Platforms: ESXi

VIRTUALPIE is a lightweight backdoor written in Python that spawns an IPv6 listener on a VMware ESXi server and features command line execution, file transfer, and reverse shell capabilities. VIRTUALPIE has been in use since at least 2022 including by UNC3886 who installed it via malicious vSphere Installation Bundles (VIBs).

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
- S1218: https://attack.mitre.org/software/S1218
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
