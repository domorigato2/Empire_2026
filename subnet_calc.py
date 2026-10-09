import ipaddress
import sys

def calculate_subnet(cidr_input):
    try:
        network = ipaddress.ip_network(cidr_input, strict=False)
    except ValueError as e:
        print(f"\n[!] Input Error: {e}\n")
        return

    total_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0

    print("\n==================================================")
    print("     CISCO CCNA // SUBNET & CIDR ARCHITECT        ")
    print("==================================================")
    print(f" Target CIDR    : {cidr_input}")
    print(f" Network ID     : {network.network_address}")
    print(f" Subnet Mask    : {network.netmask}")
    print(f" Wildcard Mask  : {network.hostmask}")
    print(f" Broadcast IP   : {network.broadcast_address}")
    print(f" Usable Hosts   : {total_hosts}")
    if total_hosts > 0:
        first_host = network.network_address + 1
        last_host = network.broadcast_address - 1
        print(f" Usable Range   : {first_host} -> {last_host}")
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        calculate_subnet(sys.argv[1])
    else:
        print("[!] Usage: python subnet_calc.py <IP/CIDR> (e.g. 192.168.1.50/24)")
