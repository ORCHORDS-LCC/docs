# S1228 PUBLOAD Outcome Lesson

## Authoritative description

- Technique: **S1228 — PUBLOAD**
- Platforms: Windows

PUBLOAD is a stager malware that has been observed installing itself in existing directories such as `C:\Users\Public` or creating new directories to stage the malware and its components. PUBLOAD malware collects details of the victim host, establishes persistence, encrypts victim details using RC4 and communicates victim details back to C2. PUBLOAD malware has previously been leveraged by China-affiliated actors identified as Mustang Panda. PUBLOAD is also known as “NoFive” and some public reporting identifies the loader component as CLAIMLOADER.

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
- S1228: https://attack.mitre.org/software/S1228
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
