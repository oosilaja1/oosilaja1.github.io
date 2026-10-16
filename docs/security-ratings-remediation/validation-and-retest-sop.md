# SOP — Finding Validation, Fix Verification & RiskRecon Retest

**Purpose:** move each RiskRecon finding from detection to a cleared rating with evidence at every step.
**Owner:** Vulnerability Management · **Tools:** RiskRecon, Qualys WAS · **NIST:** RA-5, CA-7, SI-2, SA-11

## Step 1 — Intake (RiskRecon)
1. Pull new and open findings from RiskRecon at least weekly.
2. Log each one in the tracker: finding ID, RiskRecon domain, asset (host/IP), severity, and date detected.
3. Check the asset against inventory. If it isn't ours or is orphaned, follow the [Asset Attribution SOP](asset-attribution-sop.md).

## Step 2 — Validate with Qualys WAS
1. Set up a Qualys WAS web application for the affected URL (HTTP and HTTPS), or reuse the existing one.
2. Run a scan with a profile that covers:
   - SSL/TLS protocol and cipher support, certificate validity and chain
   - HTTP → HTTPS redirect and HSTS
   - Response security headers and cookie attributes
   - Server and framework version disclosure (end-of-life detection)
   - OWASP-class application vulnerabilities, where in scope
3. Compare the WAS result with the RiskRecon finding:
   - **Confirmed** → go to Step 3.
   - **Not reproducible** → collect WAS evidence and dispute it with RiskRecon (Step 6, dispute path).
4. For non-web findings, validate with the right check instead: port scan for open services, DNS/MX lookup for SPF/DMARC.

## Step 3 — Advise the owner
Send a remediation advisory using this template:

```
Subject: [Severity] External finding on <asset> — action required by <date>

What RiskRecon reported: <finding>
What we confirmed (Qualys WAS): <specific evidence: protocol, header, version, etc.>
Why it matters: affects the organization's external security rating
Required fix: <exact configuration change / upgrade / closure>
Deadline (SLA): <date>
Reply when complete. We will rescan to verify, then request a RiskRecon retest.
```

Open a ticket for the owner team and link it in the tracker.

## Step 4 — Owner remediates
Track the ticket against the SLA (Critical 7d · High 15d · Medium 30d · Low 60d). Escalate at 75% of the SLA if there's been no progress.

## Step 5 — Verify with a Qualys WAS rescan
1. When the owner reports the fix, rescan the same target with the same profile.
2. **Pass** → save the rescan report as closure evidence.
3. **Fail** → send it back to the owner with the new evidence. The SLA clock keeps running.

## Step 6 — Request a RiskRecon retest
1. Send RiskRecon a retest request (or dispute) with:
   - Finding ID and asset
   - What changed and when
   - Qualys WAS rescan evidence (summary or screenshot)
2. Record the request date in the tracker.
3. Follow up if the finding hasn't cleared within 10 business days.

## Step 7 — Close & report
1. Close the finding once RiskRecon's retest clears it.
2. Update the monthly scorecard: grade, open findings, SLA adherence, average days to clear.

## Tracker fields

`finding_id · riskrecon_domain · finding · asset · severity · owner_team · validation_tool · detected · validated · owner_advised · owner_fixed · fix_verified_rescan · riskrecon_retest_requested · riskrecon_cleared · closure_method · nist_800_53`
