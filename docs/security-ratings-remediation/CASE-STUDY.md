# Case Study — External Attack Surface & RiskRecon Rating Remediation

**Reuben Osilaja · Attack Surface & Vulnerability Management Lead**
*Enterprise external footprint · RiskRecon · Qualys Web Application Scanning (WAS)*

> **Sanitized case study.** No organization names, domains, IP ranges, or vendor portal data. Supporting figures in the dashboard and dataset are synthetic and illustrative. The headline outcome is the real program result.

## Outcome

**Raised the organization's RiskRecon security rating from D to A in six months.** I did it by running every external finding through one repeatable loop: validate, advise, fix, verify, retest.

| Metric | Result |
|---|---|
| RiskRecon security rating | **D → A** in 6 months |
| Validation | Each web finding (HTTP/HTTPS) confirmed and diagnosed with **Qualys WAS** before going to the owner |
| Verification | Each fix re-scanned with Qualys WAS **before** RiskRecon was asked to retest |
| Closure | RiskRecon retests requested with evidence. The rating updated as findings cleared |
| Reporting | Monthly grade trajectory and burn-down to leadership and third-party risk stakeholders |

## Challenge

The organization's **RiskRecon rating had fallen to a D**. Customers, partners, insurers, and procurement teams use that grade to judge third-party risk, so it was a **business problem**, not just a technical one.

Root causes:

- **Findings without context.** RiskRecon reported issues on internet-facing assets, but the owners didn't know exactly what was wrong or how to fix it.
- **No owner for many assets.** Some attributed hosts had no known owner. A few weren't the organization's at all.
- **Edge hygiene debt.** Weak TLS, expired certificates, missing HTTPS redirects and HSTS, missing security headers, end-of-life web servers, exposed ports, and incomplete SPF / DMARC.
- **No closure loop.** Even after a fix, the rating stayed the same until RiskRecon retested. Nobody was asking for that retest.

## Approach — the remediation loop

Every RiskRecon finding went through the same seven steps:

```
1 Detect     RiskRecon flags an issue on an external asset
2 Validate   Qualys WAS scan of the HTTP/HTTPS service confirms and diagnoses it
3 Advise     Owner receives the evidence plus specific fix guidance and an SLA
4 Fix        Owner remediates (config, certificate, header, patch, port closure)
5 Verify     Qualys WAS rescan confirms the issue is gone
6 Retest     Evidence sent to RiskRecon with a retest request
7 Clear      RiskRecon retests, the finding clears, the rating updates
```

### Phase 1 — Baseline & ownership (Month 1)
- Exported every RiskRecon finding into one tracker (domain, finding, asset, severity, owner, SLA, NIST 800-53 control).
- Reconciled RiskRecon's attributed assets against the internal inventory (DNS zones, cloud accounts, certificate inventory, CMDB).
- Classified each asset as **owned & active**, **owned but orphaned**, or **not ours**, then disputed or decommissioned the last two groups.

### Phase 2 — Validate & advise with Qualys WAS (Months 1–4)
- Ran **Qualys WAS** against each affected HTTP/HTTPS service to confirm the finding, rule out false positives, and pinpoint the cause: protocol and cipher support, certificate chain, redirect behavior, response headers, cookie flags, server banners, and application vulnerabilities.
- Sent each owner a short **remediation advisory**: what was found, the evidence, the exact fix, and the deadline.
- Severity SLAs: **Critical 7 days · High 15 · Medium 30 · Low 60**.

### Phase 3 — Verify & request retest (Months 2–6)
- When an owner reported a fix, **rescanned with Qualys WAS** to confirm it before going to the vendor. Ports and email/DNS findings were confirmed with port checks and DNS lookups.
- **Contacted RiskRecon** with the verification evidence and asked for a retest, so the rating updated on the next cycle instead of waiting for routine rescans.
- Tracked each retest request until RiskRecon cleared the finding.

### Phase 4 — Report & sustain (Months 4–6)
- Gave leadership a monthly scorecard: grade trajectory, open-findings burn-down, SLA adherence, and the top RiskRecon domains.
- Set TLS and security-header baselines at the edge, plus a pre-launch Qualys WAS check for new internet-facing sites, so the grade doesn't slide back.

## What made the difference

1. **Validate before you escalate.** A Qualys WAS scan turned a vague rating finding into specific, evidence-backed fix guidance. Owners acted faster and false positives were caught early.
2. **Verify before you ask for a retest.** RiskRecon only got retest requests for fixes already confirmed by rescan, so retests cleared on the first attempt.
3. **Ask for the retest.** A fix doesn't move the rating until RiskRecon retests. Requesting it shortened the time from fix to grade change.
4. **Ownership with SLAs.** Every finding had a team, a deadline, and a weekly review.

## Control alignment

| Program activity | NIST 800-53 Rev. 5 |
|---|---|
| External asset inventory & attribution | CM-8, PM-5 |
| Continuous external monitoring (RiskRecon) | CA-7, RA-5 |
| Web application scanning & validation (Qualys WAS) | RA-5, SA-11 |
| Flaw remediation & EOL retirement | SI-2, SA-22 |
| TLS / certificate management | SC-8, SC-13, SC-17, SC-23 |
| Port & service minimization | CM-7, SC-7 |
| Email & DNS security | SC-20, SI-8 |
| Third-party risk posture reporting | PM-9, SR-6 |

ISO/IEC 27001:2022 Annex A alignment: 5.9 (inventory of assets), 8.8 (management of technical vulnerabilities), 8.20 (network security), 8.24 (use of cryptography), 8.29 (security testing in development and acceptance).

## Artifacts

- **Remediation dashboard**: grade trajectory, workflow funnel, burn-down, domain breakdown
- **Validation & retest SOP**: the Qualys WAS → owner → RiskRecon loop, step by step
- **Remediation playbook**: fix patterns for each RiskRecon domain
- **Asset attribution & dispute SOP**
- **Domain → Qualys WAS → NIST 800-53 crosswalk**
- **Synthetic findings dataset**: 120 findings with every workflow date
