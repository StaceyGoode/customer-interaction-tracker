# Customer Interaction Tracker (v3)

A realistic CRM-style dataset and script demonstrating **organized records**, **meticulous documentation**, and **data hygiene validation**.

## Fields
| Column | Description |
|---------|--------------|
| customer_name | Full name |
| date | Interaction date (YYYY-MM-DD) |
| contact_method | chat, email, or phone |
| notes | Summary of interaction |
| follow_up_date | Date for follow-up action |
| status | Pending, Completed, or On-Hold |
| agent | Assigned representative |

## Run
```
pip install pandas
python scripts/summarize_interactions.py
```
Reports created in `reports/` include customer summaries, method/status breakdowns, follow-up schedules, and validation results.