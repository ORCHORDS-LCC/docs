# Compromise Software Dependencies and Development Tools Technique Platform Profile

## Reference

- Technique: **T1195.001 — Compromise Software Dependencies and Development Tools**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications, such as pip and NPM packages, may be targeted as a means to add malicious code to users of the dependency. This may also include abandoned packages, which in some cases could be re-registered by threat actors after being removed by adversaries. Adversaries may also employ "typosquatting" or name-confusion by choosing names similar to existing popular libraries or packages in order to deceive a user. Additionally, CI/CD pipeline components, such as GitHub Actions, may be targeted in order to gain access to the building, testing, and deployment cycles of an application. By adding malicious code into a GitHub action, a threat actor may be able to collect runtime credentials (e.g., via Proc Filesystem) or insert further malicious components into the build pipelines for a second-order supply chain compromise. As GitHub Actions are often dependent on other GitHub Actions, threat actors may be able to infect a large number of repositories via the compromise of a single Action. Adversaries may also target the configuration and instruction files consumed by integrated development environments and AI coding agents. Project files such as tasks.json may execute commands when a developer opens or builds a project, while agent skill files (SKILL.md) supply an agent with instructions and resources that it loads on demand and runs with the permissions of the agent process. To encourage downloads, adversaries may publish these files under benign-appearing or typo-squatted names, upload unmodified copies of the genuine skills first so the listings accumulate installs before the content behind them is weaponized, or may place the malicious instructions in a secondary document that the reviewed entry point references. Because these artifacts are natural language or configuration rather than executable code, they may pass registry screening and signature-based scanning. Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.

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
- T1195.001: https://attack.mitre.org/techniques/T1195/001
- Reviewed: 2026-10-27
