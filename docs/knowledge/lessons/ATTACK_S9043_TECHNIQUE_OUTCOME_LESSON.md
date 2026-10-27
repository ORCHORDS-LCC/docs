# S9043 Mini Shai-Hulud Outcome Lesson

## Authoritative description

- Technique: **S9043 — Mini Shai-Hulud**
- Platforms: Containers, IaaS, Linux, macOS, SaaS, Windows

Mini Shai-Hulud is a credential stealer and self-replicating supply chain worm, derived from Shai-Hulud, that has been used by TeamPCP to target Continuous Integration and Continuous Delivery/Deployment (CI/CD) workflows since at least 2026. Mini Shai-Hulud can compromise credentials across multiple cloud, container, and AI configuration file paths and can use stolen npm and GitHub OIDC tokens to spread to other packages maintained by the compromised user. Mini Shai-Hulud also has a targeted wiper component and has used multiple C2 and data exfiltration mechanisms.

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
- S9043: https://attack.mitre.org/software/S9043
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
