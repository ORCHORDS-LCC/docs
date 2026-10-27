# Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements Attack Pattern Assurance Profile

## Reference

- Attack pattern: **208 — Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements**
- Status: Draft

## Pattern description

An attacker removes or modifies the logic on a client associated with monetary calculations resulting in incorrect information being sent to the server. A server may rely on a client to correctly compute monetary information. For example, a server might supply a price for an item and then rely on the client to correctly compute the total cost of a purchase given the number of items the user is buying. If the attacker can remove or modify the logic that controls these calculations, they can return incorrect values to the server. The attacker can use this to make purchases for a fraction of the legitimate cost or otherwise avoid correct billing for activities.

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
- 208: https://capec.mitre.org/data/definitions/208.html
- Reviewed: 2026-10-27
