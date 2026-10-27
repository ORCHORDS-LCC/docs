# T1557 Adversary-in-the-Middle Outcome Lesson

## Authoritative description

- Technique: **T1557 — Adversary-in-the-Middle**
- Tactics: credential-access, collection
- Platforms: Linux, macOS, Network Devices, Windows

Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as Network Sniffing, Transmitted Data Manipulation, or replay attacks (Exploitation for Credential Access). By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR, etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information or perform additional actions. For example, adversaries may manipulate victim DNS settings to enable other malicious activities such as preventing/redirecting users from accessing legitimate sites and/or pushing additional malware. Adversaries may also manipulate DNS and leverage their position in order to intercept user credentials, including access tokens (Steal Application Access Token) and session cookies (Steal Web Session Cookie). Downgrade Attacks can also be used to establish an AiTM position, such as by negotiating a less secure, deprecated, or weaker version of communication protocol (SSL/TLS) or encryption algorithm. Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic, such as in Transmitted Data Manipulation. Adversaries can setup a position similar to AiTM to prevent traffic from flowing to the appropriate destination, potentially to impair defenses and/or in support of a Network Denial of Service.

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
- T1557: https://attack.mitre.org/techniques/T1557
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
