# Session Credential Falsification through Forging Attack Pattern Assurance Profile

## Reference

- Attack pattern: **196 — Session Credential Falsification through Forging**
- Status: Draft

## Pattern description

An attacker creates a false but functional session credential in order to gain or usurp access to a service. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. If an attacker is able to forge valid session credentials they may be able to bypass authentication or piggy-back off some other authenticated user's session. This attack differs from Reuse of Session IDs and Session Sidejacking attacks in that in the latter attacks an attacker uses a previous or existing credential without modification while, in a forging attack, the attacker must create their own credential, although it may be based on previously observed credentials.

## Assurance profile

1. Determine whether the attack pattern is in scope for the systems and data being protected, and record the reason.
2. Review the pattern's prerequisites: the access, position, or precondition it requires.
3. Identify the observable indicators the pattern would produce in logs, telemetry, or configuration.
4. Define the control that prevents the pattern and the control that would detect it.
5. Define the verification method and the evidence that would demonstrate either prevention or detection.
6. Record the residual risk where only detection, not prevention, can be achieved.

## Verification evidence

- a scope decision recording why the pattern is or is not applicable;
- the indicator list mapped to the telemetry that would carry it;
- the control mapping with the evidence that supports it;
- a test or exercise record for the detection path.

## Limitations

An attack-pattern entry describes a class of abuse. Applicability and exposure are properties of a system, established only by evidence.

## Source

- MITRE CAPEC catalog: https://capec.mitre.org/data/xml/capec_latest.xml
- 196: https://capec.mitre.org/data/definitions/196.html
- Reviewed: 2026-10-27
