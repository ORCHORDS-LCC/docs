# USB Memory Attacks Attack Pattern Assurance Profile

## Reference

- Attack pattern: **457 — USB Memory Attacks**
- Status: Draft

## Pattern description

An adversary loads malicious code onto a USB memory stick in order to infect any system which the device is plugged in to. USB drives present a significant security risk for business and government agencies. Given the ability to integrate wireless functionality into a USB stick, it is possible to design malware that not only steals confidential data, but sniffs the network, or monitor keystrokes, and then exfiltrates the stolen data off-site via a Wireless connection. Also, viruses can be transmitted via the USB interface without the specific use of a memory stick. The attacks from USB devices are often of such sophistication that experts conclude they are not the work of single individuals, but suggest state sponsorship. These attacks can be performed by an adversary with direct access to a target system or can be executed via means such as USB Drop Attacks.

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
- 457: https://capec.mitre.org/data/definitions/457.html
- Reviewed: 2026-10-27
