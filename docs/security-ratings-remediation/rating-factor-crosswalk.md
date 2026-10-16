# Rating Factor Crosswalk — Vendors → NIST 800-53 / ISO 27001

How common external rating categories line up across platforms and map to controls. Vendor category names are paraphrased and grouped by theme; check each platform's current methodology for exact naming.

| Theme | BitSight (risk vector area) | SecurityScorecard (factor area) | RiskRecon (domain area) | NIST 800-53 Rev. 5 | ISO 27001:2022 Annex A |
|---|---|---|---|---|---|
| TLS & certificates | TLS/SSL configurations & certificates | Network security / encryption | Encryption | SC-8, SC-13, SC-17 | 8.24 |
| Exposed services | Open ports | Network security | Network filtering | CM-7, SC-7 | 8.20, 8.22 |
| Patching & EOL software | Patching cadence, server software | Patching cadence | Software patching | SI-2, RA-5, SA-22 | 8.8 |
| Web application security | Web application headers | Application security | Web application security | SC-8, SI-10 | 8.26, 8.28 |
| Email security | SPF / DKIM / DMARC | DNS health | Email security | SC-20, SI-8 | 8.20 |
| DNS hygiene | DNSSEC & DNS records | DNS health | DNS security | SC-20, SC-21, CM-8 | 8.20 |
| Asset attribution | Asset map / infrastructure | Digital footprint | Asset discovery | CM-8, PM-5 | 5.9 |
| Compromise signals | Compromised systems | Malware / IP reputation | Threat intel | SI-3, SI-4, IR-4 | 8.7, 8.16 |

## How to use it

- **Prioritize:** a finding that shows up on all three platforms affects every rating. Fix it first.
- **Evidence:** cite the NIST control in the remediation ticket so closure doubles as audit evidence (CA-7 continuous monitoring).
- **Third-party risk:** use the same crosswalk to answer customer security questionnaires consistently.
