import sys
import subprocess

def run_quick_recon(target):
    print("\n==================================================")
    print("      AUTOMATED RECONNAISSANCE SUITE // PIPELINE  ")
    print("==================================================")
    print(f" Target Objective : {target}")
    print("--------------------------------------------------")

    # Stage 1: ICMP Reachability
    print("\n[+] STAGE 1: Running ICMP Ping Reachability Scout...")
    subprocess.run([sys.executable, "ping_scout.py", target])

    # Stage 2: Multi-Threaded Port Range Scan (1 to 100 for rapid tactical probe)
    print("\n[+] STAGE 2: Running Multi-Threaded Port Range Sweep (1-100)...")
    subprocess.run([sys.executable, "port_range_scanner.py", target, "1", "100"])

    print("==================================================")
    print(" Reconnaissance Pipeline Execution Complete.")
    print("==================================================\n")

if __name__ == "__main__":
    t = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    run_quick_recon(t)
