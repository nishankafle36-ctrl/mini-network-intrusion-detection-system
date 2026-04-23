#  Mini Network Intrusion Detection System (IDS)

## Overview
This project is a simple Python-based Intrusion Detection System (IDS) that detects suspicious network activity using rule-based logic.

It monitors incoming traffic and flags:
- Repeated requests from the same IP address
- Access attempts to sensitive ports (e.g., SSH - port 22)

---

## How It Works
The system simulates network traffic and:
1. Tracks the number of requests from each IP address
2. Compares it against a defined threshold
3. Raises an alert if suspicious behavior is detected

---

## Technologies Used
- Python
- Basic data structures (dictionary, counters)

---

## How to Run

```bash
python simple_ids.py