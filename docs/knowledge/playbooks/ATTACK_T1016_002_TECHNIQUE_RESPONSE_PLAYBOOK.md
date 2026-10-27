# Wi-Fi Discovery Technique Response Playbook

## Target technique

**T1016.002 — Wi-Fi Discovery**

- Tactics: discovery
- Platforms: Linux, Windows, macOS

Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromised systems. Adversaries may use Wi-Fi information as part of Account Discovery, Remote System Discovery, and other discovery or Credential Access activity to support both ongoing and future campaigns. Adversaries may collect various types of information about Wi-Fi networks from hosts. For example, on Windows names and passwords of all Wi-Fi networks a device has previously connected to may be available through `netsh wlan show profiles` to enumerate Wi-Fi names and then `netsh wlan show profile “Wi-Fi name” key=clear` to show a Wi-Fi network’s corresponding password. Additionally, names and other details of locally reachable Wi-Fi networks can be discovered using calls to `wlanAPI.dll` Native API functions. On Linux, names and passwords of all Wi-Fi-networks a device has previously connected to may be available in files under ` /etc/NetworkManager/system-connections/`. On macOS, the password of a known Wi-Fi may be identified with ` security find-generic-password -wa wifiname` (requires admin username/password).

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
- T1016.002: https://attack.mitre.org/techniques/T1016/002
- Reviewed: 2026-10-27
