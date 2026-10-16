# Case Study — Attack Surface Management

**Reuben Osilaja · Cloud & Container Security Lead**
*Enterprise Kubernetes estate · 900+ clusters · 160,000+ workloads · 600,000+ container images*

---

### Challenge

A large, fast-growing multi-cloud Kubernetes / AKS estate had outpaced its security visibility. Clusters were being spun up faster than they could be brought under scanning, leaving **shadow workloads** unmonitored. The vulnerability scanner produced tens of thousands of findings, but raw CVSS scores gave no way to tell which ones actually mattered — so remediation stalled, backlogs grew, and end-of-life Kubernetes versions accumulated as an unmanaged risk. Leadership had no single, trustworthy view of the organization's exposure.

### Approach

I stood up a unified **Attack Surface Management** program to find everything the organization owned, understand its real exposure, and drive the risk down on a repeatable cadence:

- **Discovery & coverage** — reconciled cluster inventory against scanned inventory to surface shadow/unmonitored clusters and orphaned assets, and brought them under continuous scanning.
- **Risk-based prioritization** — replaced raw-CVSS triage with a model weighting **exploitability and business impact**, elevating confirmed, reachable attack paths above standalone findings.
- **Ownership & SLAs** — codified a clear RACI (platform team vs. cluster owner) and SLA-driven remediation so accountability no longer fell through the cracks.
- **Shift-left & runtime** — embedded image scanning, admission control, and runtime protection into CI/CD.
- **Executive reporting** — delivered real-time, control-aligned dashboards so leadership could see posture and progress at any moment.

### Tools & Frameworks

Aqua Security · Wiz (CSPM / CIEM / CWPP) · Qualys VMDR · Tenable Nessus · BitSight · RiskRecon · SecurityScorecard · Kubernetes / AKS · NIST 800-53 · ISO 27001 · FedRAMP · Power BI

### Outcomes

- **48% reduction** in critical/high CVE exposure through risk-based remediation.
- **Mean time to remediate cut from 18 → 7 days** for critical container vulnerabilities.
- **Kubernetes version-compliance raised to 85% within 30 days** by driving EOL clusters onto supported versions.
- **Shadow workloads eliminated** — full-estate scanning coverage restored, closing visibility gaps.

### Evidence (sanitized artifacts)

- **container-vuln-management** — the program: handbook, SOP suite, and ownership (RACI) model, with a sanitized 240-cluster scan dataset.
- **container-vuln-remediation-plan** — the 15-section remediation plan mapped to NIST 800-53 / ISO 27001 / FedRAMP.
- **container-vulnerability-risk-analytics** — executive risk dashboard (severity, status, cloud, top-risk clusters).
- **k8s-version-compliance-tracker** — version/EOL compliance reporting for leadership.

> *All artifacts are sanitized: methodology, templates, and synthetic data only — no employer-internal information.*
