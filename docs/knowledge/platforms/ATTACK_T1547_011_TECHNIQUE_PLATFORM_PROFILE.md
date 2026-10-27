# Plist Modification Technique Platform Profile

## Reference

- Technique: **T1547.011 — Plist Modification**
- Platforms named in the source: macOS

Adversaries can modify property list files (plist files) to execute their code as part of establishing persistence. Plist files are used by macOS applications to store properties and configuration settings for applications and services. Applications use information plist files, <code>Info.plist</code>, to tell the operating system how to handle the application at runtime using structured metadata in the form of keys and values. Plist files are formatted in XML and based on Apple's Core Foundation DTD and can be saved in text or binary format. Adversaries can modify paths to executed binaries, add command line arguments, and insert key/pair values to plist files in auto-run locations which execute upon user logon or system startup. Through modifying plist files in these locations, adversaries can also execute a malicious dynamic library (dylib) by adding a dictionary containing the <code>DYLD_INSERT_LIBRARIES</code> key combined with a path to a malicious dylib under the <code>EnvironmentVariables</code> key in a plist file. Upon user logon, the plist is called for execution and the malicious dylib is executed within the process space. Persistence can also be achieved by modifying the <code>LSEnvironment</code> key in the application's <code>Info.plist</code> file.

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
- T1547.011: https://attack.mitre.org/techniques/T1547/011
- Reviewed: 2026-10-27
