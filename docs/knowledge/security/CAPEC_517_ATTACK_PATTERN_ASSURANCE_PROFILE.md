# Documentation Alteration to Circumvent Dial-down Attack Pattern Assurance Profile

## Reference

- Attack pattern: **517 — Documentation Alteration to Circumvent Dial-down**
- Status: Draft

## Pattern description

An attacker with access to a manufacturer's documentation, which include descriptions of advanced technology and/or specific components' criticality, alters the documents to circumvent dial-down functionality requirements. This alteration would change the interpretation of implementation and manufacturing techniques, allowing for advanced technologies to remain in place even though these technologies might be restricted to certain customers, such as nations on the terrorist watch list, giving the attacker on the receiving end of a shipped product access to an advanced technology that might otherwise be restricted.

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
- 517: https://capec.mitre.org/data/definitions/517.html
- Reviewed: 2026-10-27
