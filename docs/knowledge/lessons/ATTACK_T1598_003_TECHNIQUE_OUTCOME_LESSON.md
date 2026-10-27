# T1598.003 Spearphishing Link Outcome Lesson

## Authoritative description

- Technique: **T1598.003 — Spearphishing Link**
- Tactics: reconnaissance
- Platforms: PRE

Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: Establish Accounts or Compromise Accounts) and/or sending multiple, seemingly urgent messages. All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, the malicious emails contain links generally accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser. The given website may be a clone of a legitimate site (such as an online or corporate login portal) or may closely resemble a legitimate site in appearance and have a URL containing elements from the real site. URLs may also be obfuscated by taking advantage of quirks in the URL schema, such as the acceptance of integer- or hexadecimal-based hostname formats and the automatic discarding of text before an “@” symbol: for example, `hxxp://google.com@1157586937`. Adversaries may also embed “tracking pixels,” "web bugs," or "web beacons" within phishing messages to verify the receipt of an email, while also potentially profiling and tracking victim information such as IP address. These mechanisms often appear as small images (typically one pixel in size) or otherwise obfuscated objects and are typically delivered as HTML code containing a link to a remote server. Adversaries may also be able to spoof a complete website using what is known as a "browser-in-the-browser" (BitB) attack. By generating a fake browser popup window with an HTML-based address bar that appears to contain a legitimate URL (such as an authentication portal), they may be able to prompt users to enter their credentials while bypassing typical URL verification methods. Adversaries can use phishing kits such as `EvilProxy` and `Evilginx2` to perform adversary-in-the-middle phishing by proxying the connection between the victim and the legitimate website. On a successful login, the victim is redirected to the legitimate website, while the adversary captures their session cookie (i.e., Steal Web Session Cookie) in addition to their username and password. This may enable the adversary to then bypass MFA via Web Session Cookie. Adversaries may also send a malicious link in the form of Quick Response (QR) Codes (also known as “quishing”). These links may direct a victim to a credential phishing page. By using a QR code, the URL may not be exposed in the email and may thus go undetected by most automated email security scans. These QR codes may be scanned by or delivered directly to a user’s mobile device (i.e., Phishing), which may be less secure in several relevant ways. For example, mobile users may not be able to notice minor differences between genuine and credential harvesting websites due to mobile’s smaller form factor. From the fake website, information is gathered in web forms and sent to the adversary. Adversaries may also use information from previous reconnaissance efforts (ex: Search Open Websites/Domains or Search Victim-Owned Websites) to craft persuasive and believable lures.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1598.003: https://attack.mitre.org/techniques/T1598/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
