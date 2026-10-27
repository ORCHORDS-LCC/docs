# T1557.001 Name Resolution Poisoning and SMB Relay Outcome Lesson

## Authoritative description

- Technique: **T1557.001 — Name Resolution Poisoning and SMB Relay**
- Tactics: credential-access, collection
- Platforms: Windows

By responding to LLMNR/NBT-NS/mDNS network traffic, adversaries may spoof an authoritative source for name resolution to force communication with an adversary controlled system. This activity may be used to collect or relay authentication materials. Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification. LLMNR is based upon the Domain Name System (DNS) format and allows hosts on the same local link to perform name resolution for other hosts. NBT-NS identifies systems on a local network by their NetBIOS name. Multicast Domain Name System(mDNS) is a zero-configuration service used to resolve hostnames to IP addresses with “.local” as a top-level domain. MDNS is based upon Domain Name System (DNS) format and allows hosts on the same network segment to perform name resolution for other hosts, using multicast. Adversaries can spoof an authoritative source for name resolution on a victim network by responding to LLMNR (UDP 5355)/NBT-NS (UDP 137)/mDNS (UDP 5353) traffic as if they know the identity of the requested host, effectively poisoning the service so that the victims will communicate with the adversary controlled system. If the requested host belongs to a resource that requires identification/authentication, the username and NTLMv2 hash will then be sent to the adversary controlled system. The adversary can then collect the hash information sent over the wire through tools that monitor the ports for traffic or through Network Sniffing and crack the hashes offline through Brute Force to obtain the plaintext passwords. In some cases where an adversary has access to a system that is in the authentication path between systems or when automated scans that use credentials attempt to authenticate to an adversary controlled system, the NTLMv1/v2 hashes can be intercepted and relayed to access and execute code against a target system. The relay step can happen in conjunction with poisoning but may also be independent of it. Additionally, adversaries may encapsulate the NTLMv1/v2 hashes into various other protocols, such as LDAP, MSSQL and HTTP, to expand and use multiple services with the valid NTLM response. Several tools may be used to poison name services within local networks such as NBNSpoof, Metasploit, and Responder.

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
- T1557.001: https://attack.mitre.org/techniques/T1557/001
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
