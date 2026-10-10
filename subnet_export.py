import ipaddress
import sys

def export_subnet(cidr):
    try:
        net = ipaddress.ip_network(cidr, strict=False)
    except ValueError as e:
        print(f"\n[!] Invalid CIDR format: {e}\n")
        return

    print("\n==================================================")
    print("      SUBNET HOST EXPORTER // IP MAPPING TOOL     ")
    print("==================================================")
    print(f" Target Subnet  : {net}")
    print(f" Netmask        : {net.netmask}")
    print(f" Total Addresses: {net.num_addresses}")
    print("--------------------------------------------------")
    print(" Usable Host IP Inventory:")
    
    count = 0
    for ip in net.hosts():
        count += 1
        print(f"    --> Host {count:03d}: {ip}")
        
    print("--------------------------------------------------")
    print(f" Total Usable Hosts Mapped: {count}")
    print("==================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.0/29"
    export_subnet(target)
