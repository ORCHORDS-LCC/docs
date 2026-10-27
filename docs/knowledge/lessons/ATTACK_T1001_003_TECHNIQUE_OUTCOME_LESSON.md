# T1001.003 Protocol or Service Impersonation Outcome Lesson

## Authoritative description

- Technique: **T1001.003 — Protocol or Service Impersonation**
- Tactics: command-and-control
- Platforms: ESXi, Linux, macOS, Windows

Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activity and thwart analysis efforts. By impersonating legitimate protocols or web services, adversaries can make their command and control traffic blend in with legitimate network traffic. Adversaries may impersonate a fake SSL/TLS handshake to make it look like subsequent traffic is SSL/TLS encrypted, potentially interfering with some security tooling, or to make the traffic look like it is related with a trusted entity. Adversaries may also leverage legitimate protocols to impersonate expected web traffic or trusted services. For example, adversaries may manipulate HTTP headers, URI endpoints, SSL certificates, and transmitted data to disguise C2 communications or mimic legitimate services such as Gmail, Google Drive, and Yahoo Messenger.

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
- T1001.003: https://attack.mitre.org/techniques/T1001/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
