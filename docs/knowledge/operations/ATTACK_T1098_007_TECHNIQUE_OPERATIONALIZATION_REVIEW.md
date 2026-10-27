# Additional Local or Domain Groups Technique Operationalization Review

## Reference

- Technique: **T1098.007 — Additional Local or Domain Groups**

An adversary may add additional local or domain groups to an adversary-controlled account to maintain persistent access to a system or domain. On Windows, accounts may use the `net localgroup` and `net group` commands to add existing users to local and domain groups. On Linux, adversaries may use the `usermod` command for the same purpose. For example, accounts may be added to the local administrators group on Windows devices to maintain elevated privileges. They may also be added to the Remote Desktop Users group, which allows them to leverage Remote Desktop Protocol to log into the endpoints in the future. Adversaries may also add accounts to VPN user groups to gain future persistence on the network. On Linux, accounts may be added to the sudoers group, allowing them to persistently leverage Sudo and Sudo Caching for elevated privileges. In Windows environments, machine accounts may also be added to domain groups. This allows the local SYSTEM account to gain privileges on the domain.

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
- T1098.007: https://attack.mitre.org/techniques/T1098/007
- Reviewed: 2026-10-27
