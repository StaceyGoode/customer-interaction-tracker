# Customer Interaction Tracker (Business & Operations Overview)

A structured workflow system for documenting customer communication, billing clarification, account follow-ups, and internal notes in a CRM-style format. This tracker reflects real-world behaviors of customer success and billing teams: accurate documentation, traceable follow-up scheduling, escalation visibility, and clear internal communication.

This is highly relevant to roles in billing operations, SaaS support, payment reconciliation, dispute handling, customer success, and operational administration because these teams depend on:

- Documentation accuracy and audit-readiness  
- Organized internal notes for account history  
- SLA prioritization and escalation accountability  
- Time-sensitive follow-ups  
- Professional clarity and empathy in communication  
- Cross-team visibility and process consistency  

The tracker demonstrates how a remote operations or billing-support environment can prevent lost information, streamline payment questions, and improve customer satisfaction simply through disciplined documentation.

---

For a quick structural view, open: data/customer_interactions.csv

![Sample Interaction Log](screenshot_interaction_log.png)


The Customer Interaction Tracker is a portfolio project that demonstrates my ability to maintain organized, accurate records of customer interactions in a CRM-style system.
It showcases meticulous documentation practices, automated data validation, and the generation of clear, actionable reports — skills essential for customer success, operations, or AI data-support roles.

This project automatically:

Tracks customer communications (date, method, notes, agent)

Logs follow-up dates and status updates

Validates and cleans data for consistency

Generates structured reports for summaries and follow-ups

I created this to simulate how real-world teams maintain detailed, reliable communication records.
It reflects strong attention to detail, data organization, and documentation discipline — the same skills I use to manage information efficiently and ensure nothing falls through the cracks.

Skills Demonstrated

Organized Record Management: Designed and maintained structured logs of customer interactions with consistent formatting and traceability.

Meticulous Documentation: Ensured every entry includes detailed notes, follow-up dates, and agent accountability.

Data Validation & Quality Control: Automated checks for missing, duplicate, or inconsistent data to ensure integrity.

Report Generation: Built Python scripts to create summary and follow-up reports automatically from raw data.

Analytical Thinking: Interpreted customer engagement trends using structured data outputs.

Process Automation: Streamlined repetitive documentation tasks through scripting and clean data pipelines.

Professional Communication: Produced clean, readable reports suitable for team review or management dashboards.

Version Control & Collaboration: Managed code and documentation through GitHub for transparency and version tracking.

How to Use This Project

Download or clone this repository

Click the green Code button near the top of this page and select Download ZIP.

Unzip the folder to your computer.

(Alternatively, if you use Git, you can clone it with:)

git clone https://github.com/StaceyGoode/customer-interaction-tracker.git


Install the required library
Make sure Python 3.9+ is installed, then open Terminal and run:

pip install pandas


Run the tracker
Navigate into the project folder in Terminal and run:

python3 scripts/summarize_interactions.py


View your results
After running, open the reports/ folder to find the generated files:

customer_summary.csv — per-customer overview

method_breakdown.csv — breakdown by contact method

status_breakdown.csv — summary of pending/completed interactions

followup_schedule.csv — list of upcoming follow-ups

quality_checks.json — data validation report

Customize or experiment
Open data/customer_interactions.csv in Excel, Numbers, or Google Sheets to modify or add new customer interactions.
Each time you re-run the script, updated reports will be generated automatically.
