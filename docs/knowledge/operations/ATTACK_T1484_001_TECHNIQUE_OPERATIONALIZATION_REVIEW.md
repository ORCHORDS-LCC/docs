# Group Policy Modification Technique Operationalization Review

## Reference

- Technique: **T1484.001 — Group Policy Modification**

Adversaries may modify Group Policy Objects (GPOs) to subvert the intended discretionary access controls for a domain, usually with the intention of escalating privileges on the domain. Group policy allows for centralized management of user and computer settings in Active Directory (AD). GPOs are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`. Like other objects in AD, GPOs have access controls associated with them. By default all user accounts in the domain have permission to read GPOs. It is possible to delegate GPO access control permissions, e.g. write access, to specific users or groups in the domain. Malicious GPO modifications can be used to implement many other malicious behaviors such as Scheduled Task/Job, Disable or Modify Tools, Ingress Tool Transfer, Create Account, Service Execution, and more. Since GPOs can control so many user and machine settings in the AD environment, there are a great number of potential attacks that can stem from this GPO abuse. For example, publicly available scripts such as <code>New-GPOImmediateTask</code> can be leveraged to automate the creation of a malicious Scheduled Task/Job by modifying GPO settings, in this case modifying <code>&lt;GPO_PATH&gt;\Machine\Preferences\ScheduledTasks\ScheduledTasks.xml</code>. In some cases an adversary might modify specific user rights like SeEnableDelegationPrivilege, set in <code>&lt;GPO_PATH&gt;\MACHINE\Microsoft\Windows NT\SecEdit\GptTmpl.inf</code>, to achieve a subtle AD backdoor with complete control of the domain because the user account under the adversary's control would then be able to modify GPOs.

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
- T1484.001: https://attack.mitre.org/techniques/T1484/001
- Reviewed: 2026-10-27
