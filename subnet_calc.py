import ipaddress

print("=========================================")
print("      CCNA IPv4 SUBNET CALCULATOR        ")
print("=========================================")

cidr_input = input("Enter Network/CIDR (e.g., 192.168.1.0/24): ").strip()

try:
    # strict=False allows passing host IPs like 192.168.1.50/24
    net = ipaddress.ip_network(cidr_input, strict=False)
    
    total = net.num_addresses
    usable = max(total - 2, 0)
    
    # Calculate host range in O(1) time complexity (no memory lag)
    first_host = net.network_address + 1 if total > 2 else "N/A"
    last_host = net.broadcast_address - 1 if total > 2 else "N/A"
    
    print("-----------------------------------------")
    print(f"INPUT CIDR        : {cidr_input}")
    print(f"NETWORK ID        : {net.network_address}")
    print(f"BROADCAST ID      : {net.broadcast_address}")
    print(f"SUBNET MASK       : {net.netmask}")
    print(f"TOTAL ADDRESSES   : {total}")
    print(f"USABLE HOSTS      : {usable}")
    print(f"USABLE HOST RANGE : {first_host} - {last_host}")
    print("-----------------------------------------")

except ValueError as err:
    print(f"\n[!] Invalid IPv4 CIDR syntax: {err}")

print("CALCULATION COMPLETE. PURE CCNA LOGIC.")
print("=========================================")