import sys
import time
import os

def append_log(entry_text):
    today = time.strftime("%Y-%m-%d")
    log_file = f"journal_{today}.txt"
    timestamp = time.strftime("%I:%M %p")
    
    formatted_entry = f"[{timestamp}] {entry_text}\n"
    
    with open(log_file, "a") as f:
        f.write(formatted_entry)
        
    print(f"\n[+] TELEMETRY LOGGED TO {log_file}:")
    print(f"    --> {formatted_entry.strip()}")
    print("-" * 55)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        entry = " ".join(sys.argv[1:])
        append_log(entry)
    else:
        print("[!] Usage: python empire_logger.py your log entry here")
