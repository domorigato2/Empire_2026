import re
import sys

def parse_cisco_config(filepath):
    print("\n==================================================")
    print("      CISCO CCNA // CONFIG INTERFACE EXTRACTOR    ")
    print("==================================================")
    print(f" Target Config : {filepath}")
    print(" Parsing text stream for interfaces and IPs...")
    print("--------------------------------------------------")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File '{filepath}' not found.")
        return

    # Regex to slice config into interface blocks
    interfaces = re.findall(r"interface\s+(\S+)(.*?)(?=interface\s+|\Z)", content, re.DOTALL)

    if not interfaces:
        print(" [-] No interfaces detected in configuration.")
        return

    count = 0
    for intf_name, block in interfaces:
        count += 1
        ip_match = re.search(r"ip address\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)", block)
        desc_match = re.search(r"description\s+(.+)", block)
        
        desc_str = desc_match.group(1).strip() if desc_match else "No Description"
        
        print(f" [INTF {count:02d}] {intf_name}")
        print(f"    --> Description : {desc_str}")
        if ip_match:
            print(f"    --> IPv4 Addr   : {ip_match.group(1)} / {ip_match.group(2)}")
        else:
            print(f"    --> IPv4 Addr   : Unassigned / Layer 2 Port")
        print("-" * 50)

    print(f" Extraction Complete. Total Interfaces Mapped: {count}")
    print("==================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "mock_config.txt"
    parse_cisco_config(target)
