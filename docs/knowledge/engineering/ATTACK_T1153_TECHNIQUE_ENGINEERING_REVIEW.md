# Source Technique Engineering Review

## Reference

- Technique: **T1153 — Source**

**This technique has been deprecated and should no longer be used.** The source command loads functions into the current shell or executes files in the current context. This built-in command can be run in two different ways source /path/to/filename [arguments] or .**This technique has been deprecated and should no longer be used.** /path/to/filename [arguments]. Take note of the space after the ".". Without a space, a new shell is created that runs the program instead of running the program within the current context. This is often used to make certain features or functions available to a shell or to update a specific shell's environment. Adversaries can abuse this functionality to execute programs. The file executed with this technique does not need to be marked executable beforehand.

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
- T1153: https://attack.mitre.org/techniques/T1153
- Reviewed: 2026-10-27
