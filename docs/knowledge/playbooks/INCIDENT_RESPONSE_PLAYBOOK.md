# Incident Response Playbook

## Overview

This playbook provides step-by-step procedures for responding to common security incidents. It covers detection, containment, eradication, recovery, and post-incident activities.

## Incident Classification

| Severity | Description | Response Time |
|----------|-------------|---------------|
| P1 - Critical | Active data breach, system compromise, service disruption | 15 minutes |
| P2 - High | Potential breach, significant vulnerability exploitation | 30 minutes |
| P3 - Medium | Suspicious activity, policy violation | 2 hours |
| P4 - Low | Informational, minor policy deviation | 24 hours |

## Response Phases

### Phase 1: Preparation
- Maintain incident response team contact list
- Ensure logging and monitoring are operational
- Keep runbooks and playbooks up to date
- Conduct regular tabletop exercises

### Phase 2: Detection and Analysis
- Identify the incident through monitoring, alerts, or user reports
- Classify severity and impact scope
- Preserve evidence (logs, memory dumps, network captures)
- Document timeline of events

### Phase 3: Containment
- Short-term: Isolate affected systems, block malicious IPs
- Long-term: Apply patches, reset credentials, update configurations
- Verify containment effectiveness before proceeding

### Phase 4: Eradication
- Remove malware, backdoors, and attacker access points
- Patch vulnerabilities that enabled the attack
- Verify no residual threats remain

### Phase 5: Recovery
- Restore systems from clean backups
- Monitor restored systems for signs of re-compromise
- Gradually restore normal operations

### Phase 6: Post-Incident Activity
- Conduct lessons learned meeting within 5 business days
- Document root cause, impact, and response effectiveness
- Update playbooks and controls based on findings
- Track corrective actions to completion

## Communication Templates

### Initial Notification
```
Subject: [SEVERITY] Security Incident - [Brief Description]

A security incident has been detected affecting [scope].
Initial assessment indicates [brief description].
Incident response team is investigating. Next update in [timeframe].
```

### Status Update
```
Subject: [UPDATE] Security Incident - [Brief Description]

Current status: [containment/eradication/recovery]
Impact: [affected systems/users/data]
Actions taken: [list key actions]
Next steps: [planned actions]
ETA for resolution: [timeframe]
```

### Closure Notice
```
Subject: [CLOSED] Security Incident - [Brief Description]

Incident has been resolved. Root cause: [summary].
Impact: [final assessment].
Corrective actions: [list].
Lessons learned: [key takeaways].
```

## References

- NIST SP 800-61 Rev. 2 - Computer Security Incident Handling Guide
- SANS Incident Response Process
- MITRE ATT&CK Framework for threat classification
