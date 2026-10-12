# Save as log_parser.py in C:\Users\sheil\Empire_2026\

import re

def audit_system_logs(raw_log_data):
    print("\n" + "="*60)
    print(" IT AUTOMATION // SYSTEM LOG AUDIT ENGINE")
    print("="*60)
    
    error_count = 0
    warning_count = 0
    critical_events = []
    
    for line in raw_log_data.strip().split('\n'):
        if "CRITICAL" in line or "ERROR" in line:
            error_count += 1
            critical_events.append(line.strip())
        elif "WARNING" in line:
            warning_count += 1
            
    print(f" [+] Total Lines Audited : {len(raw_log_data.strip().splitlines())}")
    print(f" [!] Warnings Detected   : {warning_count}")
    print(f" [X] Errors / Critical   : {error_count}")
    
    if critical_events:
        print("\n--- CRITICAL INCIDENT LOG ---")
        for event in critical_events:
            print(f" -> {event}")
            
    print("="*60 + "\n")

if __name__ == "__main__":
    # Simulate raw network/system log dump
    sample_logs = """
    2026-10-10 23:00:12 [INFO] Interface GigabitEthernet0/0 up
    2026-10-10 23:15:44 [WARNING] High CPU utilization detected (88%)
    2026-10-10 23:30:01 [ERROR] Authentication failure from IP 192.168.1.50
    2026-10-10 23:45:22 [INFO] BGP adjacency established with peer
    2026-10-10 23:55:10 [CRITICAL] Link down on interface Serial0/0/0
    """
    
    audit_system_logs(sample_logs)