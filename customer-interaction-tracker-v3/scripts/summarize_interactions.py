
"""
Customer Interaction Tracker (v3)

Schema:
  - customer_name
  - date
  - contact_method (chat|email|phone)
  - notes
  - follow_up_date
  - status (Pending|Completed|On-Hold)
  - agent

Outputs:
  - reports/customer_summary.csv
  - reports/method_breakdown.csv
  - reports/status_breakdown.csv
  - reports/followup_schedule.csv
  - reports/quality_checks.json
"""

import pandas as pd
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "customer_interactions.csv"
REPORTS = BASE / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

REQUIRED = ["customer_name","date","contact_method","notes","follow_up_date","status","agent"]
ALLOWED_METHODS = {"chat","email","phone"}
ALLOWED_STATUS = {"pending","completed","on-hold"}

def load_and_validate(path: Path):
    problems = []
    try:
        df = pd.read_csv(path)
    except Exception as e:
        raise SystemExit(f"Error reading CSV: {e}")

    missing_cols = [c for c in REQUIRED if c not in df.columns]
    if missing_cols:
        problems.append({"type":"missing_columns","detail":missing_cols})

    df = df[[c for c in REQUIRED if c in df.columns]]

    # Normalize text
    for c in ["customer_name","contact_method","notes","status","agent"]:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()

    df["contact_method_norm"] = df["contact_method"].str.lower()
    df["status_norm"] = df["status"].str.lower()

    # Parse dates
    for c in ["date","follow_up_date"]:
        df[c] = pd.to_datetime(df[c], errors="coerce", format="%Y-%m-%d")
        bad = df[df[c].isna()]
        if len(bad):
            problems.append({"type":"invalid_dates","column":c,"rows":bad.index.tolist()})

    # Validate enums
    bad_m = df[~df["contact_method_norm"].isin(ALLOWED_METHODS)]
    if len(bad_m):
        problems.append({"type":"invalid_contact_method","rows":bad_m.index.tolist()})

    bad_s = df[~df["status_norm"].isin(ALLOWED_STATUS)]
    if len(bad_s):
        problems.append({"type":"invalid_status","rows":bad_s.index.tolist()})

    return df, problems

def summarize(df):
    cust = df.groupby("customer_name").agg(
        interactions=("customer_name","count"),
        first_contact=("date","min"),
        last_contact=("date","max"),
        upcoming_followup=("follow_up_date","min"),
        agent=("agent", lambda x: x.mode()[0] if len(x.mode())>0 else x.iloc[0])
    ).reset_index()

    method = df.groupby("contact_method").size().reset_index(name="count")
    status = df.groupby("status").size().reset_index(name="count")
    followups = df[["customer_name","follow_up_date","status","agent"]].sort_values("follow_up_date")

    return cust, method, status, followups

def main():
    df, problems = load_and_validate(DATA)
    cust, method, status, followups = summarize(df)

    cust.to_csv(REPORTS/"customer_summary.csv", index=False)
    method.to_csv(REPORTS/"method_breakdown.csv", index=False)
    status.to_csv(REPORTS/"status_breakdown.csv", index=False)
    followups.to_csv(REPORTS/"followup_schedule.csv", index=False)

    summary = {
        "records_count": int(len(df)),
        "unique_customers": int(df["customer_name"].nunique()),
        "agents": sorted(df["agent"].unique().tolist()),
        "issues_found": problems
    }
    with open(REPORTS/"quality_checks.json","w") as f:
        json.dump(summary, f, indent=2)

    print("=== Customer Interaction Tracker (v3) ===")
    print(f"Records: {len(df)} | Unique Customers: {df['customer_name'].nunique()}")
    print("By contact method:")
    print(method.to_string(index=False))
    print("By status:")
    print(status.to_string(index=False))
    print("Reports generated in:", REPORTS)

if __name__ == "__main__":
    main()
