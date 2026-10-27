# Dumpster Diving Attack Pattern Assurance Profile

## Reference

- Attack pattern: **406 — Dumpster Diving**
- Status: Stable

## Pattern description

An adversary cases an establishment and searches through trash bins, dumpsters, or areas where company information may have been accidentally discarded for information items which may be useful to the dumpster diver. The devastating nature of the items and/or information found can be anything from medical records, resumes, personal photos and emails, bank statements, account details or information about software, tech support logs and so much more, including hardware devices. By collecting this information an adversary may be able to learn important facts about the person or organization that play a role in helping the adversary in their attack.

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
- 406: https://capec.mitre.org/data/definitions/406.html
- Reviewed: 2026-10-27
