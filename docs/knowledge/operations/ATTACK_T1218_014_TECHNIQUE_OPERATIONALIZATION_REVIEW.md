# MMC Technique Operationalization Review

## Reference

- Technique: **T1218.014 — MMC**

Adversaries may abuse mmc.exe to proxy execution of malicious .msc files. Microsoft Management Console (MMC) is a binary that may be signed by Microsoft and is used in several ways in either its GUI or in a command prompt. MMC can be used to create, open, and save custom consoles that contain administrative tools created by Microsoft, called snap-ins. These snap-ins may be used to manage Windows systems locally or remotely. MMC can also be used to open Microsoft created .msc files to manage system configuration. For example, mmc (a user home directory)admintools.msc /a will open a custom, saved console msc file in author mode. Another common example is mmc gpedit.msc, which will open the Group Policy Editor application window. Adversaries may use MMC commands to perform malicious tasks. For example, mmc wbadmin.msc delete catalog -quiet deletes the backup catalog on the system (i.e. Inhibit System Recovery) without prompts to the user (Note: wbadmin.msc may only be present by default on Windows Server operating systems). Adversaries may also abuse MMC to execute malicious .msc files. For example, adversaries may first create a malicious registry Class Identifier (CLSID) subkey, which uniquely identifies a Component Object Model class object. Then, adversaries may create custom consoles with the “Link to Web Address” snap-in that is linked to the malicious CLSID subkey. Once the .msc file is saved, adversaries may invoke the malicious CLSID payload with the following command: mmc.exe -Embedding C:\path\to\test.msc.

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
- T1218.014: https://attack.mitre.org/techniques/T1218/014
- Reviewed: 2026-10-27
