import subprocess
import re

def inspect_arp():
    print("\n==================================================")
    print("     CISCO CCNA // LAYER 2 ARP TABLE INSPECTOR    ")
    print("==================================================")
    print(" Pulling kernel ARP cache (IP -> MAC Mapping)...")
    print("--------------------------------------------------")

    try:
        output = subprocess.check_output(["arp", "-a"], universal_newlines=True)
    except Exception as e:
        print(f"[!] Extraction Failed: {e}")
        return

    found = 0
    for line in output.splitlines():
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F-]+)\s+(\w+)", line)
        if match:
            ip, mac, entry_type = match.groups()
            # Filter multicast / broadcast noise
            if not ip.startswith("224.") and not ip.startswith("239.") and not ip.endswith(".255"):
                print(f" [L3 IP] {ip:<15} --> [L2 MAC] {mac:<18} [{entry_type.upper()}]")
                found += 1

    print("--------------------------------------------------")
    print(f" Physical Adjacencies Mapped: {found}")
    print("==================================================\n")

if __name__ == "__main__":
    inspect_arp()
