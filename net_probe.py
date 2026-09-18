import subprocess

print("=========================================")
print("      CCNA NETWORK REACHABILITY PROBE    ")
print("=========================================")

# Targets based on your ipconfig telemetry
targets = [
    ("Local Default Gateway", "192.168.1.1"),
    ("Internet Backbone (Google DNS)", "8.8.8.8"),
    ("DNS Resolution Layer", "google.com")
]

for name, host in targets:
    print(f"[*] Probing {name} [{host}]...")
    # Windows ping: -n 1 (1 packet), -w 1000 (1-second timeout)
    cmd = ["ping", "-n", "1", "-w", "1000", host]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if result.returncode == 0:
        print(f"    --> [PASS] Echo reply received. Link UP.")
    else:
        print(f"    --> [FAIL] Packet dropped. Host unreachable.")

print("=========================================")
print("DIAGNOSTIC COMPLETE. HOLD THE LINE.")
print("=========================================")