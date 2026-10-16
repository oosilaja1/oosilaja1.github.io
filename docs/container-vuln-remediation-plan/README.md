# Container Vulnerability Remediation Plan (CVRP)

A **sanitized 15-section template** for a Cloud Infrastructure **Container Vulnerability Remediation Plan** — the document that converts container scanner output into **audit-ready, control-mapped evidence** aligned to NIST 800-53, ISO 27001, and FedRAMP.

> ⚠️ **Sanitized portfolio artifact.** Template and methodology only. No employer-internal data, systems, or findings. All examples are illustrative.

## What a CVRP is for

A scanner produces findings; auditors, ATO reviewers, and leadership need a **plan**. The CVRP is the bridge: it states scope, prioritization logic, SLAs, ownership, control mappings, and the POA&M linkage in one governed document — so that "we scan our containers" becomes "here is our controlled, evidenced remediation program."

## The 15 sections

The full template is in [`CVRP-template.md`](CVRP-template.md):

1. Purpose & Scope
2. Roles & Responsibilities (RACI reference)
3. Tooling & Data Sources
4. Asset & Coverage Inventory
5. Vulnerability Discovery Workflow
6. Risk-Based Prioritization Methodology
7. Remediation SLAs
8. Remediation Workflow & Verification
9. Kubernetes Version / EOL Management
10. Exceptions & Risk Acceptance
11. Continuous Monitoring
12. Metrics, KPIs & Reporting
13. Control Mapping (NIST 800-53 / ISO 27001 / FedRAMP)
14. POA&M Integration
15. Plan Maintenance & Review Cadence

## Control crosswalks

- [`control-mappings/nist-800-53-crosswalk.md`](nist-800-53-crosswalk.md)
- [`control-mappings/iso-27001-crosswalk.md`](iso-27001-crosswalk.md)
- [`control-mappings/fedramp-notes.md`](fedramp-notes.md)

## Companion repositories

- **Container Vulnerability Management Program** — the handbook, SOPs, and RACI that this plan operationalizes.
- **Kubernetes Version-Compliance Tracker** — working code for §9.

## License

[MIT License](LICENSE).
