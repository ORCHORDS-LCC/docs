# Credentials from Web Browsers Technique Engineering Review

## Reference

- Technique: **T1555.003 — Credentials from Web Browsers**

Adversaries may acquire credentials from web browsers by reading files specific to the target browser. Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers typically store the credentials in an encrypted format within a credential store; however, methods exist to extract plaintext credentials from web browsers. For example, on Windows systems, encrypted credentials may be obtained from Google Chrome by reading a database file, AppData\Local\Google\Chrome\User Data\Default\Login Data and executing a SQL query: SELECT action_url, username_value, password_value FROM logins;. The plaintext password can then be obtained by passing the encrypted credentials to the Windows API function CryptUnprotectData, which uses the victim’s cached logon credentials as the decryption key. Adversaries have executed similar procedures for common web browsers such as FireFox, Safari, Edge, etc. Windows stores Internet Explorer and Microsoft Edge credentials in Credential Lockers managed by the Windows Credential Manager. Adversaries may also acquire credentials by searching web browser process memory for patterns that commonly match credentials. After acquiring credentials from web browsers, adversaries may attempt to recycle the credentials across different systems and/or accounts in order to expand access. This can result in significantly furthering an adversary's objective in cases where credentials gained from web browsers overlap with privileged accounts (e.g. domain administrator).

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
- T1555.003: https://attack.mitre.org/techniques/T1555/003
- Reviewed: 2026-10-27
