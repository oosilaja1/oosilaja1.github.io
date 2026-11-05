# Case Study — AI Systems for Vulnerability Management & AI Governance

**Reuben Osilaja · Vulnerability Management & GRC**
*ExploitLens · Microsoft Copilot Studio · Prompt engineering · NIST 800-53 · NIST AI RMF*

---

### Challenge

Vulnerability teams don't lack data; they lack time. Findings arrive from many scanners in different formats, CVSS treats every "critical" the same whether or not anyone is exploiting it, and analysts spend hours rewriting the same facts for engineers, owners and executives. Meanwhile, organizations are switching on AI assistants such as Microsoft 365 Copilot without fixing the oversharing and access problems those assistants instantly expose.

I set out to build AI that removes the repetitive work while staying **grounded, explainable and governed**.

### What I built

**1. ExploitLens (live): exploitability analysis across every scanner**

- Imports CSV/JSON exports from **AquaSec, Kubescape, Qualys, Tenable/Nessus, Trivy and Wiz**, or pasted CVE IDs, then normalizes, merges and de-duplicates them into one queue.
- Enriches every CVE with **NVD** (CVSS, references), **CISA KEV** (confirmed exploitation, ransomware use) and **EPSS** (probability of exploitation).
- Assigns a verdict (Actively Exploited, Exploitation Likely, Exploitable – Conditions Apply, Low Exploitability, Insufficient Data), a **risk score, P1–P3 priority and SLA due date**, using exposure and asset criticality.
- Explains **"why this verdict"** and gives domain-specific remediation plus "if you can't patch yet" compensating controls.
- Produces dashboards, **executive and technical PDF reports**, and CSV exports; includes a knowledge base and CVE lookup.
- Built as a working MVP with an AI app builder (Lovable): I designed the logic, data sources, verdict rules, remediation playbooks and reports, and the builder generated the code from my specifications.

**2. AI Readiness Advisor (prototype): a Microsoft Copilot Studio agent**

- Runs a 10-question Microsoft 365 Copilot readiness self-assessment: identity, admin access, oversharing, permissions hygiene, sensitivity labels, DLP, audit logging, baseline hardening, AI policy and AI ownership.
- Scores the answers out of 20, rates readiness (Ready / Ready with gaps / Not ready), ranks the top 3 gaps by risk, and maps each to NIST 800-53 and the NIST AI RMF with a 30-day action plan.
- Hard rules keep it on-script: no credential or tenant-data collection, no claims of scanning, FedRAMP/GCC checks flagged for federal users.

**3. VM AI Prompt Library (in use): seven guarded templates**

- Multi-audience CVE reframing, escalation messaging, triage narratives, executive scorecard narratives and stand-up prep.
- Structured inputs and explicit guardrails ("use only the data provided", "write *unknown* instead of guessing") keep outputs consistent and factual.

### Challenges and how I solved them

| Challenge | Resolution |
|---|---|
| Every scanner exports a different format | Mapped each tool's fields to one common finding model and de-duplicated by CVE + asset |
| Findings arrive without asset context | Analysis-level defaults (internet-facing, criticality) that report columns can override; perimeter devices treated as internet-facing |
| Analysts must be able to defend a verdict | Every verdict shows its evidence: KEV date, ransomware use, EPSS percentile, attack vector |
| Controlling access to the tool | Access limited to approved users; sign-in email sent from my own domain |
| Copilot Studio's default environment had no Dataverse | Provisioned Dataverse, then moved the build to a dedicated development environment, separating dev from production |
| Agent usage is credit-metered per environment | Used the trial path to keep prototype cost at zero; documented credit allocation as a cost control |
| New agents start with broad access (Microsoft 365 data, web search) | Removed both before testing, applying least privilege |

### Governance approach

| Risk | Control | Mapping |
|---|---|---|
| Data exposure / oversharing | Scope agent sources; fix permissions, labels and DLP first | AC-3, AC-6, AC-21, SC-7 · AI RMF MAP |
| Inaccurate or invented output | Ground in named sources; show the "why" | RA-5, SI-10 · AI RMF MEASURE |
| Unreviewed decisions | AI recommends; people approve risk acceptance and changes | CM-3, CA-7 · AI RMF MANAGE |
| No accountability | Audit logging, retention, named AI owner and use policy | AU-2, AU-11, PL-4, PM-2 · AI RMF GOVERN |
| Uncontrolled change | Separate dev and production environments | CM-2, SA-3, SA-11 |
| Runaway cost | Per-environment credits and limits | SA-9, PM-3 |

### Status

- **ExploitLens:** live, used with synthetic demo data for showcases.
- **AI Readiness Advisor:** built and saved in Copilot Studio; end-to-end testing pending trial credits.
- **VM AI Prompt Library:** complete (7 templates).

*All screenshots and samples use synthetic data. No client or employer data is included.*
