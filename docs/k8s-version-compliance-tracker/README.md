# Kubernetes Version-Compliance Tracker

Working, dependency-free Python that reads a **cluster inventory** and a **supported-version policy**, classifies every cluster as **Supported / Near-EOL / EOL**, computes an estate-wide **version-compliance %**, and renders an **HTML dashboard** for leadership.

> ⚠️ **Sanitized portfolio artifact.** Ships with fully synthetic sample data only — no employer-internal cluster names, versions, or inventory. Standard library only, no third-party dependencies.

Running an end-of-life Kubernetes version is a vulnerability class in its own right. This tool operationalizes the version-compliance metric that a container security program reports to leadership — echoing the version-compliance tracking described in the companion **Container Vulnerability Management Program**.

## Demo output

Run against the bundled **240-cluster synthetic dataset**:

```
Kubernetes Version-Compliance  (2026-07-24)
====================================================
Clusters tracked        : 240
Supported               : 80
Near-EOL (action soon)  : 80
EOL (out of compliance) : 80
----------------------------------------------------
VERSION-COMPLIANCE      : 66.7%
====================================================
```

It also writes [`dashboard.html`](dashboard.html) — KPI tiles, a compliance gauge, and a per-cluster table sorted worst-first (EOL → Near-EOL → Supported). Open it in any browser.

## Usage

```bash
# Python 3.10+ ; no dependencies to install

# Default: the 240-cluster synthetic dataset
python3 version_compliance.py --today 2026-07-24

# Or point it at any inventory + policy
python3 version_compliance.py \
    --clusters clusters_synthetic_240.csv \
    --policy   k8s_supported_versions.csv \
    --html     dashboard.html
```

## Inputs

Two sample inventories are included:

- **`clusters_synthetic_240.csv`** — a realistic 240-cluster estate (3 clouds, 5 environments, K8s 1.34–1.36), derived from the synthetic container-vulnerability dataset shared across these repos.
- **`clusters_sample.csv`** — a minimal 12-cluster example for quick reading.

Inventory columns:

| column | example |
| --- | --- |
| `cluster_name` | `k8s-orion-pro-11` |
| `k8s_version` | `v1.34.1-sim` (accepts `1.32.4`, `v1.32`, and `-sim` suffixes) |
| `environment` | `production` / `staging` / `development` |
| `owner_team` | `Cloud Defense` |
| `last_scanned` | `2026-07-01` |

**`k8s_supported_versions.csv`** — the policy (`minor`, `eol_date`). Update this to your own support baseline.

## Classification logic

| Status | Rule |
| --- | --- |
| **EOL** | Minor version is past its end-of-life date, or older than any tracked minor. Counts as **out of compliance**. |
| **Near-EOL** | Within `NEAR_EOL_WINDOW_DAYS` (default 90) of end-of-life. Still compliant, but flagged for action. |
| **Supported** | Otherwise. |

**`version_compliance_% = (total − EOL) ÷ total × 100`**

## Companion repositories

- **[container-vuln-management](https://github.com/oosilaja1/container-vuln-management)** — the program this metric reports into (handbook, SOPs, RACI, and the source dataset).
- **[container-vulnerability-risk-analytics](https://github.com/oosilaja1/container-vulnerability-risk-analytics)** — executive risk dashboard over the same estate.

## License

[MIT License](LICENSE).
