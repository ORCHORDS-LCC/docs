# Bind Mounts Technique Engineering Review

## Reference

- Technique: **T1564.013 — Bind Mounts**

Adversaries may abuse bind mounts on file structures to hide their activity and artifacts from native utilities. A bind mount maps a directory or file from one location on the filesystem to another, similar to a shortcut on Windows. It’s commonly used to provide access to specific files or directories across different environments, such as inside containers or chroot environments, and requires sudo access. Adversaries may use bind mounts to map either an empty directory or a benign `/proc` directory to a malicious process’s `/proc` directory. Using the commands `mount –o bind /proc/benign-process /proc/malicious-process` (or `mount –B`), the malicious process's `/proc` directory is overlayed with the contents of a benign process's `/proc` directory. When system utilities query process activity, such as `ps` and `top`, the kernel follows the bind mount and presents the benign directory’s contents instead of the malicious process's actual `/proc` directory. As a result, these utilities display information that appears to come from the benign process, effectively hiding the malicious process's metadata, executable, or other artifacts from detection.

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
- T1564.013: https://attack.mitre.org/techniques/T1564/013
- Reviewed: 2026-10-27
