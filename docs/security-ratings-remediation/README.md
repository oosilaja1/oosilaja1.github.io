# RiskRecon Security Rating Remediation Program

A **sanitized reference implementation** of a program that raised an organization's **RiskRecon** security rating **from D to A in six months**. The organization was also monitored on BitSight and SecurityScorecard; the RiskRecon workstream was led personally. It uses **Qualys Web Application Scanning (WAS)** to validate findings, guide asset owners, verify fixes, and back up retest requests to RiskRecon.

> All data here is synthetic. Domains use the reserved `.example` suffix. No organization, vendor portal, or customer data is included.

## What's inside

| Artifact | Purpose |
|---|---|
| `CASE-STUDY.md` | Challenge, approach, outcome, and control alignment |
| `validation-and-retest-sop.md` | The seven-step loop: RiskRecon → Qualys WAS → owner → verify → RiskRecon retest |
| `remediation-playbook.md` | Fix patterns for each RiskRecon domain, with owners and SLAs |
| `asset-attribution-sop.md` | How to reconcile attributed assets and file disputes |
| `rating-factor-crosswalk.md` | RiskRecon domain → Qualys WAS check → NIST 800-53 / ISO 27001 |
| `synthetic-ratings-findings.csv` | 120 synthetic findings with dates for every workflow step |
| `dashboard.html` | Grade trajectory, workflow funnel, burn-down, and breakdowns |

## Operating model

```
RiskRecon finding
      │
      ▼
Qualys WAS scan (HTTP/HTTPS) ──► false positive? ──► dispute with evidence
      │ confirmed
      ▼
Remediation advisory to owner (evidence + exact fix + SLA)
      │
      ▼
Owner fixes ──► Qualys WAS rescan ──► still failing? ──► back to owner
      │ verified
      ▼
Retest request to RiskRecon (with rescan evidence)
      │
      ▼
RiskRecon retest clears finding ──► rating updates ──► monthly scorecard
```

## SLAs

| Severity | Owner remediates within |
|---|---|
| Critical | 7 days |
| High | 15 days |
| Medium | 30 days |
| Low | 60 days |
