# Case Study — External Attack Surface & Security Ratings Remediation

**Reuben Osilaja · Attack Surface & Vulnerability Management Lead**
*Enterprise external footprint · BitSight · SecurityScorecard · RiskRecon*

> **Sanitized case study.** No organization names, domains, IP ranges, or vendor portal data. Supporting figures in the dashboard and dataset are synthetic and illustrative; the headline outcome is the real program result.


## Outcome

**Raised the organization's external security rating from D to A+ in six months** — by treating security ratings as a managed attack surface program rather than a score to argue about.

| Metric | Result |
|---|---|
| Security rating | **D → A+** in 6 months |
| Ratings findings tracked to closure | Every finding owned, ticketed, and closed or formally dispositioned |
| Misattributed assets | Disputed with the rating vendors or decommissioned — removing "phantom" risk from the score |
| Reporting | Monthly rating trajectory and burn-down to leadership and third-party risk stakeholders |


## Challenge

The organization's public-facing security rating had fallen to a **D**. That grade was visible to customers, partners, insurers, and procurement teams — so it was a **business problem**, not just a technical one. Third-party risk questionnaires were coming back flagged, and nobody owned the score.

Root causes:

- **No asset ownership.** The rating vendors attributed hundreds of internet-facing assets to the organization. Many had no known owner; some were not the organization's at all.
- **Hygiene debt at the edge.** Weak or expired TLS certificates, exposed management ports, end-of-life web servers, missing security headers, and incomplete SPF / DKIM / DMARC.
- **Three platforms, three views.** BitSight, SecurityScorecard, and RiskRecon each scored differently, so teams received conflicting signals.
- **No closure loop.** Fixes happened ad hoc, and nobody verified that the rating platform had picked the fix up.


## Approach

I ran it as a six-month program in four phases.

### Phase 1 — Baseline & attribution (Month 1)
- Exported findings from **BitSight, SecurityScorecard, and RiskRecon** into one normalized tracker (platform, rating factor, asset, severity, owner, SLA, NIST 800-53 control).
- Reconciled every attributed IP and domain against the internal asset inventory (CMDB, DNS zones, cloud accounts, certificate inventory).
- Classified each asset as **Owned**, **Owned – orphaned**, or **Not ours (misattributed)**.

### Phase 2 — Quick wins & disputes (Months 1–2)
- Filed **attribution disputes** with each vendor for misattributed IPs and domains, with evidence (WHOIS, ASN ownership, hosting contracts).
- **Decommissioned orphaned assets**: dangling DNS records, retired marketing sites, forgotten test hosts.
- Closed the fastest score-moving items first: expired certificates, open RDP/SSH/database ports, and missing DMARC records.

### Phase 3 — Systemic remediation (Months 2–5)
- Set **severity-based SLAs** (Critical 7 days · High 15 · Medium 30 · Low 60) with named owner teams (Network Engineering, Cloud Platform, App Owners, Messaging, Web).
- Standardized a **TLS baseline** (TLS 1.2+, strong ciphers, HSTS) and a **web security header baseline** (CSP, X-Frame-Options, X-Content-Type-Options).
- Retired or upgraded **end-of-life web servers and frameworks** on internet-facing hosts.
- Enforced **SPF / DKIM / DMARC** across all sending domains, moving DMARC from `p=none` to `p=reject`.

### Phase 4 — Verify, govern, sustain (Months 5–6)
- **Verified closure on the rating platform**, not just in the ticket. A finding was closed only after the vendor rescan cleared it.
- Built a **monthly ratings scorecard** for leadership: grade trajectory, open findings burn-down, SLA adherence, and top risk factors.
- Added **pre-launch checks** so new internet-facing assets are registered, owned, and compliant before go-live. This stops the grade from drifting back.


## What made the difference

1. **Attribution first.** A meaningful share of the "risk" belonged to assets the organization didn't own or no longer used. Disputing and retiring them moved the score faster than any patch.
2. **One tracker, three vendors.** Normalizing all three platforms into one ledger removed conflicting priorities.
3. **Closure means vendor-verified.** Closing tickets doesn't move a rating. Confirmed rescans do.
4. **Ownership with SLAs.** Every finding had a team, a deadline, and a weekly review.


## Control alignment

| Program activity | NIST 800-53 Rev. 5 |
|---|---|
| External asset inventory & attribution | CM-8, PM-5 |
| Continuous external scanning & ratings monitoring | RA-5, CA-7 |
| Patching & EOL retirement | SI-2, SA-22 |
| TLS / certificate management | SC-8, SC-13, SC-17 |
| Port & service minimization | CM-7, SC-7 |
| Email & DNS security | SC-20, SI-8 |
| Third-party risk posture reporting | PM-9, SR-6 |

ISO/IEC 27001:2022 Annex A alignment: 5.9 (inventory of assets), 5.22 (monitoring of supplier services), 8.8 (management of technical vulnerabilities), 8.20 (network security), 8.24 (use of cryptography).


## Artifacts

- **Ratings remediation dashboard** — rating trajectory, burn-down, factor breakdown, closure methods
- **Remediation playbook** — fix patterns by rating factor
- **Asset attribution & dispute SOP**
- **Rating factor → NIST 800-53 crosswalk**
- **Synthetic findings dataset** (120 findings)
