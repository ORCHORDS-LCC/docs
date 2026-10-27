# T1048 Exfiltration Over Alternative Protocol Outcome Lesson

## Authoritative description

- Technique: **T1048 — Exfiltration Over Alternative Protocol**
- Tactics: exfiltration
- Platforms: ESXi, IaaS, Linux, macOS, Network Devices, Office Suite, SaaS, Windows

Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. Exfiltration Over Alternative Protocol can be done using various common operating system utilities such as Net/SMB or FTP. On macOS and Linux <code>curl</code> may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system. Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or Cloud API.

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
- T1048: https://attack.mitre.org/techniques/T1048
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
