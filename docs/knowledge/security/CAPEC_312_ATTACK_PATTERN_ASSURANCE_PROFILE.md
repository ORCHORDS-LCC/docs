# Active OS Fingerprinting Attack Pattern Assurance Profile

## Reference

- Attack pattern: **312 — Active OS Fingerprinting**
- Status: Stable

## Pattern description

An adversary engages in activity to detect the operating system or firmware version of a remote target by interrogating a device, server, or platform with a probe designed to solicit behavior that will reveal information about the operating systems or firmware in the environment. Operating System detection is possible because implementations of common protocols (Such as IP or TCP) differ in distinct ways. While the implementation differences are not sufficient to 'break' compatibility with the protocol the differences are detectable because the target will respond in unique ways to specific probing activity that breaks the semantic or logical rules of packet construction for a protocol. Different operating systems will have a unique response to the anomalous input, providing the basis to fingerprint the OS behavior. This type of OS fingerprinting can distinguish between operating system types and versions.

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
- 312: https://capec.mitre.org/data/definitions/312.html
- Reviewed: 2026-10-27
