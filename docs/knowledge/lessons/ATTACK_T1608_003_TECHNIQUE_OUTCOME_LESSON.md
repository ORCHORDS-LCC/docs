# T1608.003 Install Digital Certificate Outcome Lesson

## Authoritative description

- Technique: **T1608.003 — Install Digital Certificate**
- Tactics: resource-development
- Platforms: PRE

Adversaries may install SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are files that can be installed on servers to enable secure communications between systems. Digital certificates include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate securely with its owner. Certificates can be uploaded to a server, then the server can be configured to use the certificate to enable encrypted communication with it. Adversaries may install SSL/TLS certificates that can be used to further their operations, such as encrypting C2 traffic (ex: Asymmetric Cryptography with Web Protocols) or lending credibility to a credential harvesting site. Installation of digital certificates may take place for a number of server types, including web servers and email servers. Adversaries can obtain digital certificates (see Digital Certificates) or create self-signed certificates (see Digital Certificates). Digital certificates can then be installed on adversary controlled infrastructure that may have been acquired (Acquire Infrastructure) or previously compromised (Compromise Infrastructure).

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
- T1608.003: https://attack.mitre.org/techniques/T1608/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
