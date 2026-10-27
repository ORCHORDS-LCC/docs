# Encrypted/Encoded File Technique Platform Profile

## Reference

- Technique: **T1027.013 — Encrypted/Encoded File**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may encrypt or encode files to obfuscate strings, bytes, and other specific patterns to impede detection. Encrypting and/or encoding file content aims to conceal malicious artifacts within a file used in an intrusion. Many other techniques, such as Software Packing, Steganography, and Embedded Payloads, share this same broad objective. Encrypting and/or encoding files could lead to a lapse in detection of static signatures, only for this malicious content to be revealed (i.e., Deobfuscate/Decode Files or Information) at the time of execution/use. This type of file obfuscation can be applied to many file artifacts present on victim hosts, such as malware log/configuration and payload files. Files can be encrypted with a hardcoded or user-supplied key, as well as otherwise obfuscated using standard encoding schemes such as Base64. The entire content of a file may be obfuscated, or just specific functions or values (such as C2 addresses). Encryption and encoding may also be applied in redundant layers for additional protection. For example, adversaries may abuse password-protected Word documents or self-extracting (SFX) archives as a method of encrypting/encoding a file such as a Phishing payload. These files typically function by attaching the intended archived content to a decompressor stub that is executed when the file is invoked (e.g., User Execution). Adversaries may also abuse file-specific as well as custom encoding schemes. For example, Byte Order Mark (BOM) headers in text files may be abused to manipulate and obfuscate file content until Command and Scripting Interpreter execution.

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
- T1027.013: https://attack.mitre.org/techniques/T1027/013
- Reviewed: 2026-10-27
