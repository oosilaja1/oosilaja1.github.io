#!/usr/bin/env python3
"""
Kubernetes Version-Compliance Tracker
=====================================

Reads a cluster inventory and a supported-version policy, classifies every
cluster as Supported / Near-EOL / EOL, computes an estate-wide
version-compliance percentage, and renders an HTML dashboard.

This is a sanitized portfolio artifact: it uses only the Python standard
library and ships with illustrative sample data. No employer-internal data.

Usage
-----
    python3 version_compliance.py \
        --clusters clusters_sample.csv \
        --policy   k8s_supported_versions.csv \
        --html     dashboard.html

Inputs
------
clusters CSV : cluster_name, k8s_version, environment, owner_team, last_scanned
policy   CSV : minor, eol_date (YYYY-MM-DD)

Compliance rule
---------------
    EOL       -> minor past its end-of-life date, or older than any tracked minor
    Near-EOL  -> within NEAR_EOL_WINDOW_DAYS of end-of-life
    Supported -> otherwise
    version_compliance_% = (clusters that are NOT EOL) / (total clusters) * 100
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import re
import sys
from dataclasses import dataclass

NEAR_EOL_WINDOW_DAYS = 90


# --------------------------------------------------------------------------- #
# Parsing helpers
# --------------------------------------------------------------------------- #
def parse_minor(version: str) -> tuple[int, int] | None:
    """Extract (major, minor) from strings like 'v1.28.3', '1.30', '1.27.x'."""
    m = re.search(r"(\d+)\.(\d+)", version.strip().lstrip("vV"))
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def load_policy(path: str) -> dict[tuple[int, int], dt.date]:
    """Return {(major, minor): eol_date}."""
    policy: dict[tuple[int, int], dt.date] = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            key = parse_minor(row["minor"])
            if key is None:
                continue
            policy[key] = dt.date.fromisoformat(row["eol_date"].strip())
    if not policy:
        sys.exit(f"error: no valid rows in policy file {path!r}")
    return policy


# --------------------------------------------------------------------------- #
# Classification
# --------------------------------------------------------------------------- #
@dataclass
class ClusterResult:
    cluster_name: str
    k8s_version: str
    environment: str
    owner_team: str
    last_scanned: str
    status: str          # Supported | Near-EOL | EOL | Unknown
    days_to_eol: int | None


def classify(row: dict, policy: dict[tuple[int, int], dt.date],
             today: dt.date) -> ClusterResult:
    minor = parse_minor(row.get("k8s_version", ""))
    oldest_tracked = min(policy) if policy else None

    if minor is None:
        status, days = "Unknown", None
    elif minor in policy:
        days = (policy[minor] - today).days
        if days < 0:
            status = "EOL"
        elif days <= NEAR_EOL_WINDOW_DAYS:
            status = "Near-EOL"
        else:
            status = "Supported"
    elif oldest_tracked is not None and minor < oldest_tracked:
        # older than anything we still track -> definitively EOL
        status, days = "EOL", None
    else:
        # newer than tracked policy -> treat as supported (ahead of baseline)
        status, days = "Supported", None

    return ClusterResult(
        cluster_name=row.get("cluster_name", "").strip(),
        k8s_version=row.get("k8s_version", "").strip(),
        environment=row.get("environment", "").strip(),
        owner_team=row.get("owner_team", "").strip(),
        last_scanned=row.get("last_scanned", "").strip(),
        status=status,
        days_to_eol=days,
    )


def analyze(clusters_path: str, policy_path: str,
            today: dt.date) -> tuple[list[ClusterResult], dict]:
    policy = load_policy(policy_path)
    with open(clusters_path, newline="", encoding="utf-8") as fh:
        results = [classify(row, policy, today) for row in csv.DictReader(fh)]

    total = len(results)
    counts = {s: sum(r.status == s for r in results)
              for s in ("Supported", "Near-EOL", "EOL", "Unknown")}
    non_eol = total - counts["EOL"]
    compliance = round(100 * non_eol / total, 1) if total else 0.0

    summary = {
        "total": total,
        "counts": counts,
        "compliance_pct": compliance,
        "generated": today.isoformat(),
    }
    return results, summary


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def print_console(results: list[ClusterResult], summary: dict) -> None:
    print(f"\nKubernetes Version-Compliance  ({summary['generated']})")
    print("=" * 52)
    print(f"Clusters tracked        : {summary['total']}")
    print(f"Supported               : {summary['counts']['Supported']}")
    print(f"Near-EOL (action soon)  : {summary['counts']['Near-EOL']}")
    print(f"EOL (out of compliance) : {summary['counts']['EOL']}")
    if summary["counts"]["Unknown"]:
        print(f"Unknown version         : {summary['counts']['Unknown']}")
    print("-" * 52)
    print(f"VERSION-COMPLIANCE      : {summary['compliance_pct']}%")
    print("=" * 52)

    at_risk = [r for r in results if r.status in ("EOL", "Near-EOL")]
    if at_risk:
        print("\nAction required:")
        for r in sorted(at_risk, key=lambda x: (x.status != "EOL",
                                                x.days_to_eol or -9999)):
            eol = "past EOL" if r.status == "EOL" else f"{r.days_to_eol}d to EOL"
            print(f"  [{r.status:<8}] {r.cluster_name:<22} "
                  f"{r.k8s_version:<9} {r.environment:<6} "
                  f"{r.owner_team:<18} ({eol})")
    print()


_STATUS_COLOR = {
    "Supported": "#1a7f37",
    "Near-EOL": "#9a6700",
    "EOL": "#cf222e",
    "Unknown": "#57606a",
}


def render_html(results: list[ClusterResult], summary: dict, path: str) -> None:
    c = summary["counts"]

    def tile(label: str, value, color: str) -> str:
        return (f'<div class="tile"><div class="v" style="color:{color}">'
                f'{value}</div><div class="l">{html.escape(label)}</div></div>')

    rows = []
    order = {"EOL": 0, "Near-EOL": 1, "Unknown": 2, "Supported": 3}
    for r in sorted(results, key=lambda x: (order.get(x.status, 9),
                                            x.days_to_eol if x.days_to_eol
                                            is not None else 9999)):
        eol_txt = ("—" if r.days_to_eol is None
                   else "past EOL" if r.days_to_eol < 0
                   else f"{r.days_to_eol} days")
        rows.append(
            "<tr>"
            f"<td>{html.escape(r.cluster_name)}</td>"
            f"<td><code>{html.escape(r.k8s_version)}</code></td>"
            f"<td>{html.escape(r.environment)}</td>"
            f"<td>{html.escape(r.owner_team)}</td>"
            f'<td><span class="badge" style="background:{_STATUS_COLOR[r.status]}">'
            f"{r.status}</span></td>"
            f"<td>{eol_txt}</td>"
            f"<td>{html.escape(r.last_scanned)}</td>"
            "</tr>"
        )

    pct = summary["compliance_pct"]
    pct_color = "#1a7f37" if pct >= 90 else "#9a6700" if pct >= 75 else "#cf222e"

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kubernetes Version-Compliance</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{ font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
          margin: 0; background: #f6f8fa; color: #1f2328; }}
  .wrap {{ max-width: 1000px; margin: 0 auto; padding: 32px 20px; }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  .sub {{ color: #57606a; font-size: 13px; margin-bottom: 24px; }}
  .tiles {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(150px,1fr));
            gap: 14px; margin-bottom: 12px; }}
  .tile {{ background: #fff; border: 1px solid #d0d7de; border-radius: 10px;
           padding: 18px; text-align: center; }}
  .tile .v {{ font-size: 30px; font-weight: 700; }}
  .tile .l {{ font-size: 12px; color: #57606a; margin-top: 4px; text-transform: uppercase;
              letter-spacing: .04em; }}
  .hero {{ background:#fff; border:1px solid #d0d7de; border-radius:10px; padding:20px;
           margin-bottom:22px; display:flex; align-items:center; gap:20px; }}
  .gauge {{ font-size:44px; font-weight:800; color:{pct_color}; }}
  .bar {{ flex:1; height:14px; background:#e6e9ec; border-radius:8px; overflow:hidden; }}
  .bar > i {{ display:block; height:100%; width:{pct}%; background:{pct_color}; }}
  table {{ width: 100%; border-collapse: collapse; background:#fff;
           border:1px solid #d0d7de; border-radius:10px; overflow:hidden; }}
  th, td {{ text-align: left; padding: 10px 12px; font-size: 13px;
            border-bottom: 1px solid #eaeef2; }}
  th {{ background:#f6f8fa; font-size:11px; text-transform:uppercase; letter-spacing:.04em;
        color:#57606a; }}
  code {{ background:#eff1f3; padding:1px 6px; border-radius:5px; font-size:12px; }}
  .badge {{ color:#fff; padding:2px 9px; border-radius:20px; font-size:11px; font-weight:600; }}
  .foot {{ color:#57606a; font-size:12px; margin-top:18px; }}
</style></head>
<body><div class="wrap">
  <h1>Kubernetes Version-Compliance</h1>
  <div class="sub">Estate snapshot &middot; generated {summary['generated']} &middot; sanitized sample data</div>

  <div class="hero">
    <div class="gauge">{pct}%</div>
    <div style="flex:1">
      <div style="font-weight:600;margin-bottom:6px">Version-compliance (non-EOL clusters)</div>
      <div class="bar"><i></i></div>
    </div>
  </div>

  <div class="tiles">
    {tile("Clusters tracked", summary['total'], "#1f2328")}
    {tile("Supported", c['Supported'], _STATUS_COLOR['Supported'])}
    {tile("Near-EOL", c['Near-EOL'], _STATUS_COLOR['Near-EOL'])}
    {tile("EOL", c['EOL'], _STATUS_COLOR['EOL'])}
  </div>

  <table>
    <thead><tr><th>Cluster</th><th>Version</th><th>Env</th><th>Owner team</th>
    <th>Status</th><th>Time to EOL</th><th>Last scanned</th></tr></thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>

  <div class="foot">Sanitized portfolio artifact &middot; standard-library Python &middot;
  compliance = (total &minus; EOL) &divide; total. Near-EOL window = {NEAR_EOL_WINDOW_DAYS} days.</div>
</div></body></html>"""

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(doc)


# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Kubernetes version-compliance tracker")
    ap.add_argument("--clusters", default="clusters_synthetic_240.csv")
    ap.add_argument("--policy", default="k8s_supported_versions.csv")
    ap.add_argument("--html", default="dashboard.html")
    ap.add_argument("--today", default=None,
                    help="override 'today' as YYYY-MM-DD (default: system date)")
    args = ap.parse_args(argv)

    today = (dt.date.fromisoformat(args.today) if args.today
             else dt.date.today())

    results, summary = analyze(args.clusters, args.policy, today)
    print_console(results, summary)
    render_html(results, summary, args.html)
    print(f"HTML dashboard written to {args.html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
