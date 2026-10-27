# T1016.002 Wi-Fi Discovery Outcome Lesson

## Authoritative description

- Technique: **T1016.002 — Wi-Fi Discovery**
- Tactics: discovery
- Platforms: Linux, Windows, macOS

Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromised systems. Adversaries may use Wi-Fi information as part of Account Discovery, Remote System Discovery, and other discovery or Credential Access activity to support both ongoing and future campaigns. Adversaries may collect various types of information about Wi-Fi networks from hosts. For example, on Windows names and passwords of all Wi-Fi networks a device has previously connected to may be available through `netsh wlan show profiles` to enumerate Wi-Fi names and then `netsh wlan show profile “Wi-Fi name” key=clear` to show a Wi-Fi network’s corresponding password. Additionally, names and other details of locally reachable Wi-Fi networks can be discovered using calls to `wlanAPI.dll` Native API functions. On Linux, names and passwords of all Wi-Fi-networks a device has previously connected to may be available in files under ` /etc/NetworkManager/system-connections/`. On macOS, the password of a known Wi-Fi may be identified with ` security find-generic-password -wa wifiname` (requires admin username/password).

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
- T1016.002: https://attack.mitre.org/techniques/T1016/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
