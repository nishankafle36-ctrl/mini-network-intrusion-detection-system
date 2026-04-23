# Import defaultdict to store counts easily
from collections import defaultdict

# Import time to slow down output (just for better visualization)
import time


# STEP 1: Simulated Network Traffic
# Each tuple represents (IP Address, Port Number)
traffic_logs = [
    ("192.168.1.10", 80),
    ("192.168.1.10", 80),
    ("192.168.1.10", 80),
    ("192.168.1.10", 80),
    ("10.0.0.5", 22),
    ("192.168.1.10", 80),
]

# STEP 2: Store Request Count
# This dictionary will store how many times each IP appears
request_counter = defaultdict(int)


# STEP 3: Set Threshold
# If an IP sends more requests than this, we flag it
THRESHOLD = 4

# STEP 4: Sensitive Ports
# Some ports (like 22 for SSH) are important and should be monitored
SUSPICIOUS_PORTS = [22, 23]

print("Starting Simple Intrusion Detection System...\n")


# STEP 5: Process Traffic
for ip, port in traffic_logs:
    
    # Increase count for this IP
    request_counter[ip] += 1

    # Print normal traffic info
    print(f"[INFO] Traffic from {ip} on port {port}")


    # STEP 6: Check for suspicious ports

    if port in SUSPICIOUS_PORTS:
        print(f"[WARNING] Access attempt on sensitive port {port} from {ip}")


    # STEP 7: Check for too many requests
    
    if request_counter[ip] > THRESHOLD:
        print(f"[ALERT] Too many requests from {ip} (Possible attack!)\n")

    # Small delay so output is readable
    time.sleep(0.5)