# Remediation Playbook — RiskRecon Domains

Standard fixes for the RiskRecon findings that most often pull the rating down. Every web finding is **validated with Qualys WAS before the owner is advised** and **re-verified with a Qualys WAS rescan before RiskRecon is asked to retest**. A finding closes only when RiskRecon's retest clears it. The full loop is in the [Validation & Retest SOP](validation-and-retest-sop.md).


## 1. TLS / SSL configuration
**Typical findings:** TLS 1.0/1.1 enabled, weak ciphers, missing HSTS, insecure renegotiation.
**Owner:** Network Engineering · **SLA:** High 15d / Medium 30d · **NIST:** SC-8, SC-13

**Fix**
- Allow only TLS 1.2 and 1.3. Use AEAD cipher suites with forward secrecy.
- Add `Strict-Transport-Security: max-age=31536000; includeSubDomains`.
- Apply the baseline at the load balancer, CDN, or WAF edge so it covers every host behind it.

**Verify:** Qualys WAS rescan (protocols, ciphers, HSTS), then request a RiskRecon retest.


## 2. Expired, self-signed, or mismatched certificates
**Owner:** Network Engineering · **SLA:** High 15d · **NIST:** SC-17, IA-5

**Fix**
- Reissue certificates from a trusted CA and automate renewal (ACME or the cloud certificate manager).
- Keep a certificate inventory with expiry alerts at 30, 14, and 7 days.
- If the host is no longer needed, decommission it instead of renewing.

**Verify:** Qualys WAS rescan of certificate validity and chain, then request a RiskRecon retest.


## 3. Exposed services / open ports
**Typical findings:** RDP, SSH, SMB, database ports, or admin panels reachable from the internet.
**Owner:** Cloud Platform · **SLA:** Critical 7d / High 15d · **NIST:** CM-7, SC-7

**Fix**
- Close the port at the security group or firewall. Move admin access behind VPN, ZTNA, or a bastion host.
- Restrict any service that must stay exposed to known source IPs.
- Add a cloud guardrail policy that blocks `0.0.0.0/0` on management ports.

**Verify:** external port scan shows the port closed or filtered, then request a RiskRecon retest.


## 4. Unpatched / end-of-life software
**Typical findings:** outdated web servers, CMS platforms, frameworks, or OS versions detected in banners.
**Owner:** Application Owners · **SLA:** Critical 7d / High 15d / Medium 30d · **NIST:** SI-2, RA-5, SA-22

**Fix**
- Upgrade to a supported version. If you can't, isolate the host behind a WAF and record a time-bound risk acceptance.
- Suppress version banners as defense in depth. This is not a substitute for patching.
- Add EOL dates to the asset register so upgrades are planned before support ends.

**Verify:** Qualys WAS rescan shows the supported version (or no version disclosure plus owner confirmation), then request a RiskRecon retest.


## 5. Web application security headers
**Typical findings:** missing CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy; insecure cookies.
**Owner:** Web / AppDev · **SLA:** Medium 30d / Low 60d · **NIST:** SC-8, SI-10

**Fix**: apply a header baseline at the CDN or reverse proxy.
```
Content-Security-Policy: default-src 'self'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Set-Cookie: ...; Secure; HttpOnly; SameSite=Lax
```

**Verify:** Qualys WAS rescan of response headers and cookie flags, then request a RiskRecon retest.


## 6. Email security — SPF / DKIM / DMARC
**Owner:** Messaging · **SLA:** High 15d · **NIST:** SC-20, SI-8

**Fix**
- Publish SPF with every legitimate sender and end it in `-all`.
- Sign outbound mail with DKIM (2048-bit keys).
- Roll DMARC out in stages: `p=none` (monitor) → `p=quarantine` → `p=reject`, reviewing aggregate reports at each step.
- Give parked, non-sending domains `v=spf1 -all` and `p=reject`.

**Verify:** DNS lookup of the SPF and DMARC records, then request a RiskRecon retest.


## 7. DNS hygiene / dangling records
**Typical findings:** CNAMEs pointing to deleted cloud resources (subdomain takeover risk), stale A records.
**Owner:** Network Engineering · **SLA:** High 15d · **NIST:** CM-8, SC-20

**Fix**
- Delete records that point to resources you no longer own.
- Review DNS zones quarterly against the asset inventory.


## 8. Misattributed or orphaned assets
**Owner:** Vulnerability Management · **SLA:** Medium 30d · **NIST:** CM-8, PM-5

**Fix:** follow the [Asset Attribution & Dispute SOP](asset-attribution-sop.md). Dispute assets that aren't yours with RiskRecon, with evidence, and decommission the ones that are yours but unused.


## Prioritization rule

Fix first what moves the rating most for the least effort:

1. Misattributed assets (dispute) and orphaned assets (decommission)
2. Critical exposed services
3. Expired certificates and missing DMARC
4. TLS baseline at the edge
5. EOL software upgrades
6. Header baseline
