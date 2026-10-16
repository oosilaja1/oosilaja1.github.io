# Security Ratings Remediation Program

A **sanitized reference implementation** of a program that manages external security ratings (BitSight, SecurityScorecard, RiskRecon) as an attack surface workstream. It took an organization's rating **from D to A+ in six months**.

> All data here is synthetic. Domains use the reserved `.example` suffix. No organization, vendor portal, or customer data is included.

## What's inside

| Artifact | Purpose |
|---|---|
| `CASE-STUDY.md` | Challenge, approach, outcome, and control alignment |
| `remediation-playbook.md` | Fix patterns for each rating factor, with owners and SLAs |
| `asset-attribution-sop.md` | How to reconcile vendor-attributed assets and file disputes |
| `rating-factor-crosswalk.md` | Rating factors across the three vendors → NIST 800-53 / ISO 27001 |
| `synthetic-ratings-findings.csv` | 120 synthetic findings with owner, SLA, closure method, and NIST mapping |
| `dashboard.html` | Rating trajectory, burn-down, and remediation breakdown |

## Operating model

```
Vendor findings (BitSight · SecurityScorecard · RiskRecon)
        │  weekly export
        ▼
Normalize → one tracker (factor · asset · severity · owner · SLA · control)
        │
        ├── Not ours?        → Attribution dispute with evidence
        ├── Ours, unused?    → Decommission + DNS cleanup
        └── Ours, in use?    → Ticket to owner team under SLA
                                   │
                                   ▼
                     Vendor rescan confirms → Close
                                   │
                                   ▼
             Monthly scorecard to leadership & third-party risk
```

## SLAs

| Severity | Remediate within |
|---|---|
| Critical | 7 days |
| High | 15 days |
| Medium | 30 days |
| Low | 60 days |
