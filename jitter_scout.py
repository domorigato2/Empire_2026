import subprocess
import sys
import re

def analyze_jitter(target_host, count=10):
    print("\n==================================================================")
    print("      LAYER 3 JITTER & PACKET DELAY VARIATION SCOUT               ")
    print("==================================================================")
    print(f" Target Node  : {target_host}")
    print(f" Probing Link : Dispatching {count} high-frequency ICMP packets...")
    print("------------------------------------------------------------------")

    cmd = ["ping", "-n", str(count), target_host]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
    except Exception as e:
        print(f"[!] Execution Failure: {e}")
        return

    # Extract all individual millisecond times
    rtts = [int(m) for m in re.findall(r"time[<=](\d+)ms", output)]

    if not rtts:
        print(" [!] Link Failure: Zero ICMP replies intercepted. Target offline.")
        print("==================================================================\n")
        return

    min_rtt = min(rtts)
    max_rtt = max(rtts)
    avg_rtt = sum(rtts) / len(rtts)

    # Calculate Jitter: Average absolute difference between consecutive packets
    diffs = [abs(rtts[i] - rtts[i-1]) for i in range(1, len(rtts))]
    jitter = sum(diffs) / len(diffs) if diffs else 0.0

    # Line Stability Rating
    if jitter <= 2.0:
        stability = "[PRISTINE // FIBER-GRADE LINE QUALITY]"
    elif jitter <= 8.0:
        stability = "[STABLE // STANDARD BROADBAND LINK]"
    else:
        stability = "[UNSTABLE // HIGH JITTER DETECTED]"

    print(f" Packets Intercepted : {len(rtts)}/{count}")
    print(f" Minimum Latency     : {min_rtt} ms")
    print(f" Maximum Latency     : {max_rtt} ms")
    print(f" Average Latency     : {avg_rtt:.1f} ms")
    print(f" Jitter (Variance)   : {jitter:.2f} ms")
    print(f" Link Rating         : {stability}")
    print("==================================================================\n")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "1.1.1.1"
    cnt = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    analyze_jitter(host, cnt)
