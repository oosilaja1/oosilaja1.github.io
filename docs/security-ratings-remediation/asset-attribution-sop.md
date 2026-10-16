# SOP — External Asset Attribution & Rating Disputes

**Purpose:** make sure the RiskRecon rating reflects assets the organization actually owns and operates.
**Owner:** Vulnerability Management · **Cadence:** baseline once, then monthly · **NIST:** CM-8, PM-5, RA-5


## 1. Export
1. Export the IPs, domains, and subdomains that RiskRecon attributes to the organization.
2. Remove duplicates by IP and FQDN.

## 2. Reconcile
Match each asset against these internal sources:

| Source | What it confirms |
|---|---|
| CMDB / asset inventory | Business owner and application |
| Authoritative DNS zones | The organization controls the name |
| Cloud accounts (public IPs, load balancers, CDN) | The organization hosts it |
| ASN / IP allocation records | The organization owns the IP range |
| Certificate inventory | Active services in use |

## 3. Classify

| Class | Definition | Action |
|---|---|---|
| **Owned – active** | In inventory with a known owner | Remediate under SLA |
| **Owned – orphaned** | Ours, but no owner and no business need | Decommission and remove DNS |
| **Not ours** | Third party, previous IP holder, or shared hosting | File a dispute |
| **Shared / third-party hosted** | A vendor runs the service under our name | Route to vendor management; contractual fix |

## 4. Dispute (for "Not ours")
1. Collect evidence: WHOIS and ASN records, cloud provider IP release confirmation, contract end dates, and a DNS history screenshot.
2. Submit the dispute to RiskRecon through its asset correction process.
3. Record the dispute ID, submission date, and evidence location in the tracker.
4. Follow up after 10 business days. Close the item only when RiskRecon removes the asset.

## 5. Decommission (for "Owned – orphaned")
1. Confirm there is no business need: owner sign-off, or 14 days of notice with no objection.
2. Shut the service down, release the IP, and delete the DNS records.
3. Ask RiskRecon to retest, and confirm the asset no longer appears.

## 6. Prevent drift
- New internet-facing assets must be registered with an owner **before** go-live.
- Run a monthly delta review: every newly attributed asset gets classified within 5 business days.
