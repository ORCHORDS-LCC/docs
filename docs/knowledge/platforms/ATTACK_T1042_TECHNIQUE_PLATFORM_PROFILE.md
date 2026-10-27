# Change Default File Association Technique Platform Profile

## Reference

- Technique: **T1042 — Change Default File Association**
- Platforms named in the source: Windows

When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened. System file associations are listed under HKEY_CLASSES_ROOT\.[extension], for example HKEY_CLASSES_ROOT\.txt. The entries point to a handler for that extension located at HKEY_CLASSES_ROOT\[handler]. The various commands are then listed as subkeys underneath the shell key at HKEY_CLASSES_ROOT\[handler]\shell\[action]\command. For example: * HKEY_CLASSES_ROOT\txtfile\shell\open\command * HKEY_CLASSES_ROOT\txtfile\shell\print\command * HKEY_CLASSES_ROOT\txtfile\shell\printto\command The values of the keys listed are commands that are executed when the handler opens the file extension. Adversaries can modify these values to continually execute arbitrary commands.

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
- T1042: https://attack.mitre.org/techniques/T1042
- Reviewed: 2026-10-27
