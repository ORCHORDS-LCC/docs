# T1218.014 MMC Outcome Lesson

## Authoritative description

- Technique: **T1218.014 — MMC**
- Tactics: stealth
- Platforms: Windows

Adversaries may abuse mmc.exe to proxy execution of malicious .msc files. Microsoft Management Console (MMC) is a binary that may be signed by Microsoft and is used in several ways in either its GUI or in a command prompt. MMC can be used to create, open, and save custom consoles that contain administrative tools created by Microsoft, called snap-ins. These snap-ins may be used to manage Windows systems locally or remotely. MMC can also be used to open Microsoft created .msc files to manage system configuration. For example, mmc (a user home directory)admintools.msc /a will open a custom, saved console msc file in author mode. Another common example is mmc gpedit.msc, which will open the Group Policy Editor application window. Adversaries may use MMC commands to perform malicious tasks. For example, mmc wbadmin.msc delete catalog -quiet deletes the backup catalog on the system (i.e. Inhibit System Recovery) without prompts to the user (Note: wbadmin.msc may only be present by default on Windows Server operating systems). Adversaries may also abuse MMC to execute malicious .msc files. For example, adversaries may first create a malicious registry Class Identifier (CLSID) subkey, which uniquely identifies a Component Object Model class object. Then, adversaries may create custom consoles with the “Link to Web Address” snap-in that is linked to the malicious CLSID subkey. Once the .msc file is saved, adversaries may invoke the malicious CLSID payload with the following command: mmc.exe -Embedding C:\path\to\test.msc.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1218.014: https://attack.mitre.org/techniques/T1218/014
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
