import subprocess
import sys
import re

def trace_route(target, max_hops=12):
    print("\n==================================================")
    print("      TACTICAL ROUTE HOP SCOUT // TRACEROUTE     ")
    print("==================================================")
    print(f" Target Host : {target}")
    print(f" Max Hops    : {max_hops}")
    print(" Mapping Layer 3 router transit path...")
    print("--------------------------------------------------")

    cmd = ["tracert", "-d", "-h", str(max_hops), target]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in iter(proc.stdout.readline, ""):
            match = re.search(r"^\s*(\d+)\s+([<\d\s*ms]+)\s+(\d+\.\d+\.\d+\.\d+)", line)
            if match:
                hop_num, rtt, hop_ip = match.groups()
                clean_rtt = " ".join(rtt.split())
                print(f" [HOP {int(hop_num):02d}] --> {hop_ip:<16} | RTT: {clean_rtt}")
            elif "Request timed out" in line:
                hop_match = re.search(r"^\s*(\d+)", line)
                if hop_match:
                    h = hop_match.group(1)
                    print(f" [HOP {int(h):02d}] --> * * * [FIREWALL / FILTERED DROP]")
        proc.stdout.close()
        proc.wait()
    except Exception as e:
        print(f"[!] Trace Anomaly: {e}")

    print("==================================================\n")

if __name__ == "__main__":
    dest = sys.argv[1] if len(sys.argv) > 1 else "1.1.1.1"
    hops = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    trace_route(dest, hops)
