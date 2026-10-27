# Browser Extensions Technique Platform Profile

## Reference

- Technique: **T1176.001 — Browser Extensions**
- Platforms named in the source: Linux, Windows, macOS

Adversaries may abuse internet browser extensions to establish persistent access to victim systems. Browser extensions or plugins are small programs that can add functionality to and customize aspects of internet browsers. They can be installed directly via a local file or custom URL or through a browser's app store - an official online platform where users can browse, install, and manage extensions for a specific web browser. Extensions generally inherit the web browser's permissions previously granted. Malicious extensions can be installed into a browser through malicious app store downloads masquerading as legitimate extensions, through social engineering, or by an adversary that has already compromised a system. Security can be limited on browser app stores, so it may not be difficult for malicious extensions to defeat automated scanners. Depending on the browser, adversaries may also manipulate an extension's update url to install updates from an adversary-controlled server or manipulate the mobile configuration file to silently install additional extensions. Adversaries may abuse how chromium-based browsers load extensions by modifying or replacing the Preferences and/or Secure Preferences files to silently install malicious extensions. When the browser is not running, adversaries can alter these files, ensuring the extension is loaded, granted desired permissions, and will persist in browser sessions. This method does not require user consent and extensions are silently loaded in the background from disk or from the browser's trusted store. Previous to macOS 11, adversaries could silently install browser extensions via the command line using the <code>profiles</code> tool to install malicious <code>.mobileconfig</code> files. In macOS 11+, the use of the <code>profiles</code> tool can no longer install configuration profiles; however, <code>.mobileconfig</code> files can be planted and installed with user interaction. Once the extension is installed, it can browse to websites in the background, steal all information that a user enters into a browser (including credentials), and be used as an installer for a RAT for persistence. There have also been instances of botnets using a persistent backdoor through malicious Chrome extensions for Command and Control. Adversaries may also use browser extensions to modify browser permissions and components, privacy settings, and other security controls for Stealth.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1176.001: https://attack.mitre.org/techniques/T1176/001
- Reviewed: 2026-10-27
