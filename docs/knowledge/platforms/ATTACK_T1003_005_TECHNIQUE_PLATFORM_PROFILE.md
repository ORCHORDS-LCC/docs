# Cached Domain Credentials Technique Platform Profile

## Reference

- Technique: **T1003.005 — Cached Domain Credentials**
- Platforms named in the source: Windows, Linux

Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event a domain controller is unavailable. On Windows Vista and newer, the hash format is DCC2 (Domain Cached Credentials version 2) hash, also known as MS-Cache v2 hash. The number of default cached credentials varies and can be altered per system. This hash does not allow pass-the-hash style attacks, and instead requires Password Cracking to recover the plaintext password. On Linux systems, Active Directory credentials can be accessed through caches maintained by software like System Security Services Daemon (SSSD) or Quest Authentication Services (formerly VAS). Cached credential hashes are typically located at `/var/lib/sss/db/cache.[domain].ldb` for SSSD or `/var/opt/quest/vas/authcache/vas_auth.vdb` for Quest. Adversaries can use utilities, such as `tdbdump`, on these database files to dump the cached hashes and use Password Cracking to obtain the plaintext password. With SYSTEM or sudo access, the tools/utilities such as Mimikatz, Reg, and secretsdump.py for Windows or Linikatz for Linux can be used to extract the cached credentials. Note: Cached credentials for Windows Vista are derived using PBKDF2.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1003.005: https://attack.mitre.org/techniques/T1003/005
- Reviewed: 2026-10-27
