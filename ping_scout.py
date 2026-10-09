import subprocess
import sys
import re

def ping_host(target):
    print("\n==================================================")
    print("      TACTICAL ICMP PING // REACHABILITY PROBE    ")
    print("==================================================")
    print(f" Target Host : {target}")
    print(" Dispatching 4 ICMP Echo Requests...")
    print("--------------------------------------------------")

    cmd = ["ping", "-n", "4", target]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        output = e.output

    loss_match = re.search(r"\((\d+)%\s+loss\)", output)
    loss = loss_match.group(1) if loss_match else "100"

    avg_match = re.search(r"Average\s+=\s+(\d+ms)", output)
    avg_rtt = avg_match.group(1) if avg_match else "N/A"

    if loss == "0":
        status = "[ONLINE // REACHABLE]"
    elif int(loss) < 100:
        status = "[UNSTABLE // PACKET LOSS DETECTED]"
    else:
        status = "[OFFLINE // UNREACHABLE]"

    print(f" Reachability Status : {status}")
    print(f" Packet Loss Rate    : {loss}%")
    print(f" Average Latency RTT : {avg_rtt}")
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ping_host(sys.argv[1])
    else:
        print("[!] Usage: python ping_scout.py <HOST_OR_IP>")
