# Plist Modification Technique Response Playbook

## Target technique

**T1547.011 — Plist Modification**

- Tactics: persistence, privilege-escalation
- Platforms: macOS

Adversaries can modify property list files (plist files) to execute their code as part of establishing persistence. Plist files are used by macOS applications to store properties and configuration settings for applications and services. Applications use information plist files, <code>Info.plist</code>, to tell the operating system how to handle the application at runtime using structured metadata in the form of keys and values. Plist files are formatted in XML and based on Apple's Core Foundation DTD and can be saved in text or binary format. Adversaries can modify paths to executed binaries, add command line arguments, and insert key/pair values to plist files in auto-run locations which execute upon user logon or system startup. Through modifying plist files in these locations, adversaries can also execute a malicious dynamic library (dylib) by adding a dictionary containing the <code>DYLD_INSERT_LIBRARIES</code> key combined with a path to a malicious dylib under the <code>EnvironmentVariables</code> key in a plist file. Upon user logon, the plist is called for execution and the malicious dylib is executed within the process space. Persistence can also be achieved by modifying the <code>LSEnvironment</code> key in the application's <code>Info.plist</code> file.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1547.011: https://attack.mitre.org/techniques/T1547/011
- Reviewed: 2026-10-27
