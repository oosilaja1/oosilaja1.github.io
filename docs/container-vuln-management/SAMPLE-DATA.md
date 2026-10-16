# Sample Data — Synthetic Container Vulnerability Dataset

A **fully synthetic** container vulnerability scan dataset used to demonstrate this program's risk-based prioritization, SLAs, and reporting on realistic-looking data.

> ⚠️ **Sanitized & synthetic.** Every value is invented for this dataset. Endpoints use `.invalid`, registries use `.example`, vulnerability IDs are synthetic `SYN-…` identifiers, and all owners/emails are fictional. No employer-internal data of any kind.

## Files

| File | Contents |
| --- | --- |
| `synthetic-container-vuln-dataset.xlsx` | The full workbook: **Findings**, **Executive Summary**, **Insights**, and a **Data Dictionary** with the sanitization notice. |
| `synthetic-findings.csv` | The Findings sheet as CSV, ready for tooling. |

## Shape

- **240 clusters**, 26 fields each.
- 3 simulated clouds (Azure/AWS/GCP-Sim), 5 environments (Production, Staging, Development, Sandbox, Testing).
- Kubernetes versions 1.34–1.36 (`-sim` suffix denotes simulated versions).
- Severity totals: ~2.4K Critical, ~28K High, ~71K Medium, ~20K Low (~122K findings).
- Risk scores 6.8–100; statuses Escalated / In Remediation / Monitoring.

## How it's used

- The **[k8s-version-compliance-tracker](https://github.com/oosilaja1/k8s-version-compliance-tracker)** ingests these clusters to compute version/EOL compliance.
- The **[container-vulnerability-risk-analytics](https://github.com/oosilaja1/container-vulnerability-risk-analytics)** tool turns it into an executive risk dashboard.
- It illustrates the prioritization model and SLAs described in this repository's handbook and SOPs.
