# Accessing/Intercepting/Modifying HTTP Cookies Attack Pattern Assurance Profile

## Reference

- Attack pattern: **31 — Accessing/Intercepting/Modifying HTTP Cookies**
- Status: Draft

## Pattern description

This attack relies on the use of HTTP Cookies to store credentials, state information and other critical data on client systems. There are several different forms of this attack. The first form of this attack involves accessing HTTP Cookies to mine for potentially sensitive data contained therein. The second form involves intercepting this data as it is transmitted from client to server. This intercepted information is then used by the adversary to impersonate the remote user/session. The third form is when the cookie's content is modified by the adversary before it is sent back to the server. Here the adversary seeks to convince the target server to operate on this falsified information.

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
- 31: https://capec.mitre.org/data/definitions/31.html
- Reviewed: 2026-10-27
