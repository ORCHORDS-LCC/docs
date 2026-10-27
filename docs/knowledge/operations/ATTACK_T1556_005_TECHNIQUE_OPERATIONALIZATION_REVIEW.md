# Reversible Encryption Technique Operationalization Review

## Reference

- Technique: **T1556.005 — Reversible Encryption**

An adversary may abuse Active Directory authentication encryption properties to gain access to credentials on Windows systems. The <code>AllowReversiblePasswordEncryption</code> property specifies whether reversible password encryption for an account is enabled or disabled. By default this property is disabled (instead storing user credentials as the output of one-way hashing functions) and should not be enabled unless legacy or other software require it. If the property is enabled and/or a user changes their password after it is enabled, an adversary may be able to obtain the plaintext of passwords created/changed after the property was enabled. To decrypt the passwords, an adversary needs four components: 1. Encrypted password (<code>G$RADIUSCHAP</code>) from the Active Directory user-structure <code>userParameters</code> 2. 16 byte randomly-generated value (<code>G$RADIUSCHAPKEY</code>) also from <code>userParameters</code> 3. Global LSA secret (<code>G$MSRADIUSCHAPKEY</code>) 4. Static key hardcoded in the Remote Access Subauthentication DLL (<code>RASSFM.DLL</code>) With this information, an adversary may be able to reproduce the encryption key and subsequently decrypt the encrypted password value. An adversary may set this property at various scopes through Local Group Policy Editor, user properties, Fine-Grained Password Policy (FGPP), or via the ActiveDirectory PowerShell module. For example, an adversary may implement and apply a FGPP to users or groups if the Domain Functional Level is set to "Windows Server 2008" or higher. In PowerShell, an adversary may make associated changes to user settings using commands similar to <code>Set-ADUser -AllowReversiblePasswordEncryption $true</code>.

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
- T1556.005: https://attack.mitre.org/techniques/T1556/005
- Reviewed: 2026-10-27
