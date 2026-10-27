# T1003.005 Cached Domain Credentials Outcome Lesson

## Authoritative description

- Technique: **T1003.005 — Cached Domain Credentials**
- Tactics: credential-access
- Platforms: Windows, Linux

Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event a domain controller is unavailable. On Windows Vista and newer, the hash format is DCC2 (Domain Cached Credentials version 2) hash, also known as MS-Cache v2 hash. The number of default cached credentials varies and can be altered per system. This hash does not allow pass-the-hash style attacks, and instead requires Password Cracking to recover the plaintext password. On Linux systems, Active Directory credentials can be accessed through caches maintained by software like System Security Services Daemon (SSSD) or Quest Authentication Services (formerly VAS). Cached credential hashes are typically located at `/var/lib/sss/db/cache.[domain].ldb` for SSSD or `/var/opt/quest/vas/authcache/vas_auth.vdb` for Quest. Adversaries can use utilities, such as `tdbdump`, on these database files to dump the cached hashes and use Password Cracking to obtain the plaintext password. With SYSTEM or sudo access, the tools/utilities such as Mimikatz, Reg, and secretsdump.py for Windows or Linikatz for Linux can be used to extract the cached credentials. Note: Cached credentials for Windows Vista are derived using PBKDF2.

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
- T1003.005: https://attack.mitre.org/techniques/T1003/005
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
