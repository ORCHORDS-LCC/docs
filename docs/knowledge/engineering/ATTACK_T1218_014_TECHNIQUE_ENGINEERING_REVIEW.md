# MMC Technique Engineering Review

## Reference

- Technique: **T1218.014 — MMC**

Adversaries may abuse mmc.exe to proxy execution of malicious .msc files. Microsoft Management Console (MMC) is a binary that may be signed by Microsoft and is used in several ways in either its GUI or in a command prompt. MMC can be used to create, open, and save custom consoles that contain administrative tools created by Microsoft, called snap-ins. These snap-ins may be used to manage Windows systems locally or remotely. MMC can also be used to open Microsoft created .msc files to manage system configuration. For example, mmc (a user home directory)admintools.msc /a will open a custom, saved console msc file in author mode. Another common example is mmc gpedit.msc, which will open the Group Policy Editor application window. Adversaries may use MMC commands to perform malicious tasks. For example, mmc wbadmin.msc delete catalog -quiet deletes the backup catalog on the system (i.e. Inhibit System Recovery) without prompts to the user (Note: wbadmin.msc may only be present by default on Windows Server operating systems). Adversaries may also abuse MMC to execute malicious .msc files. For example, adversaries may first create a malicious registry Class Identifier (CLSID) subkey, which uniquely identifies a Component Object Model class object. Then, adversaries may create custom consoles with the “Link to Web Address” snap-in that is linked to the malicious CLSID subkey. Once the .msc file is saved, adversaries may invoke the malicious CLSID payload with the following command: mmc.exe -Embedding C:\path\to\test.msc.

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
- T1218.014: https://attack.mitre.org/techniques/T1218/014
- Reviewed: 2026-10-27
