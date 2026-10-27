# Lock Bumping Attack Pattern Assurance Profile

## Reference

- Attack pattern: **392 — Lock Bumping**
- Status: Draft

## Pattern description

An attacker uses a bump key to force a lock on a building or facility and gain entry. Lock Bumping is the use of a special type of key that can be tapped or bumped to cause the pins within the lock to fall into temporary alignment, allowing the lock to be opened. Lock bumping allows an attacker to open a lock without having the correct key. A standard lock is secured by a set of internal pins that prevent the device from turning. Spring loaded driver pins push down on the key pins. When the correct key is inserted, the ridges on the key push the key pins up and against the driver pins, causing correct alignment which allows the lock cylinder to rotate. A bump key is a specially constructed key that exploits this design. When the bump key is struck or firmly tapped, its teeth transfer the force of the tap into the key pins, causing the lock to momentarily shift into proper alignment for the mechanism to be opened.

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
- 392: https://capec.mitre.org/data/definitions/392.html
- Reviewed: 2026-10-27
