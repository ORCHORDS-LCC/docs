# Pretexting via Tech Support Attack Pattern Assurance Profile

## Reference

- Attack pattern: **413 — Pretexting via Tech Support**
- Status: Draft

## Pattern description

An adversary engages in pretexting behavior, assuming the role of a tech support worker, to solicit information from target persons, or manipulate the target into performing an action that serves the adversary's interests. An adversary who uses social engineering to impersonate a tech support worker can have devastating effects on a network. This is an effective attack vector, because it can give an adversary physical access to network computers. It only takes a matter of seconds for someone to compromise a computer with physical access. One of the best technological tools at the disposal of a social engineer, posing as a technical support person, is a USB thumb drive. These are small, easy to conceal, and can be loaded with different payloads depending on what task needs to be done. However, this form of attack does not require physical access as it can also be effectively carried out via phone or email.

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
- 413: https://capec.mitre.org/data/definitions/413.html
- Reviewed: 2026-10-27
