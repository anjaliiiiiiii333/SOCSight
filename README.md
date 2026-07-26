# 🛡️ SOCSight: Python & Flask Security Monitoring Platform

SOCSight is an in-progress security monitoring dashboard designed to ingest system logs, detect anomalous or malicious activity, and simulate enterprise SOC alerting workflows.

## 🚀 Key Features
* **Log Ingestion:** Parses incoming system and authentication logs for analysis.
* **Threat Detection Engine:** Uses signature-matching rules to flag suspicious activities (e.g., failed login attempts, unauthorized access).
* **Web UI Dashboard:** Built with Flask to visually display active security alerts and metrics to analysts.

## 💻 Skills & Core Concepts Demonstrated
* **Backend Development:** Routing, session handling, and application logic using Python and Flask.
* **Data Parsing:** Utilizing string manipulation and Regular Expressions (Regex) to extract IP addresses, timestamps, and usernames from raw logs.
* **Defensive Security Ops:** Designing custom alert rules based on common attack frameworks (like MITRE ATT&CK).

## ⚙️ How It Works (Under the Hood)
1. Logs are fed into the application via [Specify your method here: e.g., a file upload / local directory listener].
2. The detection script runs regex patterns to identify patterns like `Failed password for invalid user`.
3. If an anomaly threshold is breached, a high-severity alert object is created and pushed to the Flask UI.

## 📸 Dashboard Preview
[Insert a screenshot of your local Flask UI here later!]
