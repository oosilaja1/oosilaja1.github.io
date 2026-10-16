# Cloud Infrastructure Container Vulnerability Remediation Plan (CVRP)

> **Sanitized template.** Replace bracketed `[...]` placeholders. Generic methodology only — no employer-internal data.

| | |
| --- | --- |
| **Document owner** | [Container Security Lead] |
| **Version** | [x.y] |
| **Review cadence** | [Quarterly] |
| **Classification** | [Internal] |

---

## 1. Purpose & Scope

Define the objective (govern remediation of container/Kubernetes vulnerabilities across the estate) and the boundary: images (build + registry), running workloads, CI/CD pipelines, base images, and Kubernetes platform versions. State explicit exclusions and their owners.

## 2. Roles & Responsibilities

Reference the RACI. Name the Accountable party for the *process* (Container Security) and the Accountable party for the *fix* (cluster/service owners). Identify GRC sign-off authority for exceptions.

## 3. Tooling & Data Sources

List discovery and context sources and what each authoritatively provides:

| Source | Authoritative for |
| --- | --- |
| Container scanner (image/registry/CI/CD/runtime) | Vulnerability presence in images/workloads |
| CNAPP / CSPM | Reachability, attack path, misconfiguration, identity exposure |
| Cluster inventory / CMDB | Asset population & ownership |
| Threat intel (KEV / EPSS) | Exploitability enrichment |

## 4. Asset & Coverage Inventory

Define how the authoritative cluster/workload inventory is maintained and how **coverage %** (scanned ÷ total) is measured. Describe coverage reconciliation to detect shadow/unmonitored clusters.

## 5. Vulnerability Discovery Workflow

Document the build-time → registry → admission-control → runtime flow and rescan cadence. Reference SOP-01.

## 6. Risk-Based Prioritization Methodology

State the composite model: **severity × exploitability × exposure × business criticality**. Define how confirmed attack-path / toxic-combination findings are elevated above standalone CVEs. Include the tier definitions (P1–P4). This section is the audit-critical justification for *why* findings are worked in a given order.

## 7. Remediation SLAs

| Tier | Definition | Target MTTR |
| --- | --- | --- |
| P1 | Exploitable / confirmed attack path | [7 days] |
| P2 | Critical/high, reachable | [14 days] |
| P3 | Critical/high, not reachable | [30 days] |
| P4 | Medium/low | [90 days / next release] |

## 8. Remediation Workflow & Verification

Ownership routing, fix types, and the **verification rule**: closure requires a clean rescan, never owner assertion. Define MTTR measurement (confirmation → verified fix).

## 9. Kubernetes Version / EOL Management

Supported-version baseline, EOL detection, upgrade SLAs, and the estate **version-compliance %** target. Reference the companion tracker.

## 10. Exceptions & Risk Acceptance

Time-boxed exceptions only: compensating controls, residual-risk rating, hard expiry, GRC sign-off, POA&M linkage. Auto-reopen on expiry.

## 11. Continuous Monitoring

Continuous registry rescans, runtime monitoring, and drift detection. Define what "continuous" means operationally (cadence, triggers) to satisfy ConMon expectations.

## 12. Metrics, KPIs & Reporting

Core KPIs: MTTR (P1/P2 trend), critical/high exposure trend, coverage %, version-compliance %, open-exception pipeline. Define reporting cadence and audiences (ops vs leadership vs audit).

## 13. Control Mapping

Map each program activity to control families across frameworks — see `control-mappings/`. Summary:

| Activity | NIST 800-53 | ISO 27001 (A.) | 
| --- | --- | --- |
| Vulnerability scanning | RA-5 | A.8.8 |
| Flaw remediation | SI-2 | A.8.8 |
| Configuration/inventory | CM-2, CM-6, CM-8 | A.8.9 |
| Secure CI/CD / dev testing | SA-11, SA-15 | A.8.25–A.8.28 |
| Runtime / software integrity | SI-3, SI-7 | A.8.7 |
| Continuous monitoring | CA-7 | A.8.16 |
| POA&M / risk tracking | CA-5, PM-4 | A.5.* |

## 14. POA&M Integration

Define how unremediated/accepted findings become POA&M entries, the required fields, and how remediation closure updates the POA&M — the linkage that makes the program ATO-ready.

## 15. Plan Maintenance & Review Cadence

Owner, review frequency, change history table, and triggers for out-of-cycle revision (new framework baseline, major tooling change, major incident).

---

### Change history

| Version | Date | Author | Summary |
| --- | --- | --- | --- |
| [0.1] | [date] | [author] | Initial draft |
