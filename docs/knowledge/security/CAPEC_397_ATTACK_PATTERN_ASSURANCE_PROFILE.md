# Cloning Magnetic Strip Cards Attack Pattern Assurance Profile

## Reference

- Attack pattern: **397 — Cloning Magnetic Strip Cards**
- Status: Draft

## Pattern description

An attacker duplicates the data on a Magnetic strip card (i.e. 'swipe card' or 'magstripe') to gain unauthorized access to a physical location or a person's private information. Magstripe cards encode data on a band of iron-based magnetic particles arrayed in a stripe along a rectangular card. Most magstripe card data formats conform to ISO standards 7810, 7811, 7813, 8583, and 4909. The primary advantage of magstripe technology is ease of encoding and portability, but this also renders magnetic strip cards susceptible to unauthorized duplication. If magstripe cards are used for access control, all an attacker need do is obtain a valid card long enough to make a copy of the card and then return the card to its location (i.e. a co-worker's desk). Magstripe reader/writers are widely available as well as software for analyzing data encoded on the cards. By swiping a valid card, it becomes trivial to make any number of duplicates that function as the original.

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
- 397: https://capec.mitre.org/data/definitions/397.html
- Reviewed: 2026-10-27
