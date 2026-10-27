# MMC Technique Platform Profile

## Reference

- Technique: **T1218.014 — MMC**
- Platforms named in the source: Windows

Adversaries may abuse mmc.exe to proxy execution of malicious .msc files. Microsoft Management Console (MMC) is a binary that may be signed by Microsoft and is used in several ways in either its GUI or in a command prompt. MMC can be used to create, open, and save custom consoles that contain administrative tools created by Microsoft, called snap-ins. These snap-ins may be used to manage Windows systems locally or remotely. MMC can also be used to open Microsoft created .msc files to manage system configuration. For example, <code>mmc (a user home directory)admintools.msc /a</code> will open a custom, saved console msc file in author mode. Another common example is <code>mmc gpedit.msc</code>, which will open the Group Policy Editor application window. Adversaries may use MMC commands to perform malicious tasks. For example, <code>mmc wbadmin.msc delete catalog -quiet</code> deletes the backup catalog on the system (i.e. Inhibit System Recovery) without prompts to the user (Note: <code>wbadmin.msc</code> may only be present by default on Windows Server operating systems). Adversaries may also abuse MMC to execute malicious .msc files. For example, adversaries may first create a malicious registry Class Identifier (CLSID) subkey, which uniquely identifies a Component Object Model class object. Then, adversaries may create custom consoles with the “Link to Web Address” snap-in that is linked to the malicious CLSID subkey. Once the .msc file is saved, adversaries may invoke the malicious CLSID payload with the following command: <code>mmc.exe -Embedding C:\path\to\test.msc</code>.

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
- T1218.014: https://attack.mitre.org/techniques/T1218/014
- Reviewed: 2026-10-27
