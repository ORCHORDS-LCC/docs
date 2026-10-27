# Lock Picking Attack Pattern Assurance Profile

## Reference

- Attack pattern: **393 — Lock Picking**
- Status: Draft

## Pattern description

An attacker uses lock picking tools and techniques to bypass the locks on a building or facility. Lock picking is the use of a special set of tools to manipulate the pins within a lock. Different sets of tools are required for each type of lock. Lock picking attacks have the advantage of being non-invasive in that if performed correctly the lock will not be damaged. A standard lock pin-and-tumbler lock is secured by a set of internal pins that prevent the tumbler device from turning. Spring loaded driver pins push down on the key pins preventing rotation so that the bolt remains in a locked position.. When the correct key is inserted, the ridges on the key push the key pins up and against the driver pins, causing correct alignment which allows the lock cylinder to rotate. Most common locks, such as domestic locks in the US, can be picked using a standard 2 tools (i.e. a torsion wrench and a hook pick).

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
- 393: https://capec.mitre.org/data/definitions/393.html
- Reviewed: 2026-10-27
