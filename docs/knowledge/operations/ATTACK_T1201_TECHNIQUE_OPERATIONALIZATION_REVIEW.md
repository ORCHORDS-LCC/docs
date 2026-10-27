# Password Policy Discovery Technique Operationalization Review

## Reference

- Technique: **T1201 — Password Policy Discovery**

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through Brute Force. This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts). Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as net accounts (/domain), Get-ADDefaultDomainPasswordPolicy, chage -l <username>, cat /etc/pam.d/common-password, and pwpolicy getaccountpolicies . Adversaries may also leverage a Network Device CLI on network devices to discover password policy information (e.g. show aaa, show aaa common-criteria policy all). Password policies can be discovered in cloud environments using available APIs such as GetAccountPasswordPolicy in AWS .

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
- T1201: https://attack.mitre.org/techniques/T1201
- Reviewed: 2026-10-27
