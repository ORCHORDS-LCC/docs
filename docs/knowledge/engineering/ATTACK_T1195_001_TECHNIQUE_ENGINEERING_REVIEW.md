# Compromise Software Dependencies and Development Tools Technique Engineering Review

## Reference

- Technique: **T1195.001 — Compromise Software Dependencies and Development Tools**

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications, such as pip and NPM packages, may be targeted as a means to add malicious code to users of the dependency. This may also include abandoned packages, which in some cases could be re-registered by threat actors after being removed by adversaries. Adversaries may also employ "typosquatting" or name-confusion by choosing names similar to existing popular libraries or packages in order to deceive a user. Additionally, CI/CD pipeline components, such as GitHub Actions, may be targeted in order to gain access to the building, testing, and deployment cycles of an application. By adding malicious code into a GitHub action, a threat actor may be able to collect runtime credentials (e.g., via Proc Filesystem) or insert further malicious components into the build pipelines for a second-order supply chain compromise. As GitHub Actions are often dependent on other GitHub Actions, threat actors may be able to infect a large number of repositories via the compromise of a single Action. Adversaries may also target the configuration and instruction files consumed by integrated development environments and AI coding agents. Project files such as tasks.json may execute commands when a developer opens or builds a project, while agent skill files (SKILL.md) supply an agent with instructions and resources that it loads on demand and runs with the permissions of the agent process. To encourage downloads, adversaries may publish these files under benign-appearing or typo-squatted names, upload unmodified copies of the genuine skills first so the listings accumulate installs before the content behind them is weaponized, or may place the malicious instructions in a secondary document that the reviewed entry point references. Because these artifacts are natural language or configuration rather than executable code, they may pass registry screening and signature-based scanning. Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1195.001: https://attack.mitre.org/techniques/T1195/001
- Reviewed: 2026-10-27
