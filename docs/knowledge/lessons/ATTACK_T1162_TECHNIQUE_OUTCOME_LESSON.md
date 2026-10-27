# T1162 Login Item Outcome Lesson

## Authoritative description

- Technique: **T1162 — Login Item**
- Tactics: persistence
- Platforms: macOS

MacOS provides the option to list specific applications to run when a user logs in. These applications run under the logged in user's context, and will be started every time the user logs in. Login items installed using the Service Management Framework are not visible in the System Preferences and can only be removed by the application that created them . Users have direct control over login items installed using a shared file list which are also visible in System Preferences . These login items are stored in the user's ~/Library/Preferences/ directory in a plist file called com.apple.loginitems.plist . Some of these applications can open visible dialogs to the user, but they don’t all have to since there is an option to ‘Hide’ the window. If an adversary can register their own login item or modified an existing one, then they can use it to execute their code for a persistence mechanism each time the user logs in . The API method SMLoginItemSetEnabled can be used to set Login Items, but scripting languages like AppleScript can do this as well .

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
- T1162: https://attack.mitre.org/techniques/T1162
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
