# Target Influence via Framing Attack Pattern Assurance Profile

## Reference

- Attack pattern: **425 — Target Influence via Framing**
- Status: Draft

## Pattern description

An adversary uses framing techniques to contextualize a conversation so that the target is more likely to be influenced by the adversary's point of view. Framing is information and experiences in life that alter the way we react to decisions we must make. This type of persuasive technique exploits the way people are conditioned to perceive data and its significance, while avoiding negative or avoidance responses from the target. Rather than a specific technique framing is a methodology of conversation that slowly encourages the target to adopt to the adversary's perspective. One technique of framing is to avoid the use of the word "No" and to contextualize responses in a manner that is positive. When performed skillfully the target is much more likely to volunteer information or perform actions favorable to the adversary.

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
- 425: https://capec.mitre.org/data/definitions/425.html
- Reviewed: 2026-10-27
