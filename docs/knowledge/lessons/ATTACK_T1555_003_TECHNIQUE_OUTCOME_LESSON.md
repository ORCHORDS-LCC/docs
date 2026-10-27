# T1555.003 Credentials from Web Browsers Outcome Lesson

## Authoritative description

- Technique: **T1555.003 — Credentials from Web Browsers**
- Tactics: credential-access
- Platforms: Linux, macOS, Windows

Adversaries may acquire credentials from web browsers by reading files specific to the target browser. Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers typically store the credentials in an encrypted format within a credential store; however, methods exist to extract plaintext credentials from web browsers. For example, on Windows systems, encrypted credentials may be obtained from Google Chrome by reading a database file, AppData\Local\Google\Chrome\User Data\Default\Login Data and executing a SQL query: SELECT action_url, username_value, password_value FROM logins;. The plaintext password can then be obtained by passing the encrypted credentials to the Windows API function CryptUnprotectData, which uses the victim’s cached logon credentials as the decryption key. Adversaries have executed similar procedures for common web browsers such as FireFox, Safari, Edge, etc. Windows stores Internet Explorer and Microsoft Edge credentials in Credential Lockers managed by the Windows Credential Manager. Adversaries may also acquire credentials by searching web browser process memory for patterns that commonly match credentials. After acquiring credentials from web browsers, adversaries may attempt to recycle the credentials across different systems and/or accounts in order to expand access. This can result in significantly furthering an adversary's objective in cases where credentials gained from web browsers overlap with privileged accounts (e.g. domain administrator).

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
- T1555.003: https://attack.mitre.org/techniques/T1555/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
