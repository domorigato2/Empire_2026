import ipaddress
import sys

def convert_mask(prefix_or_mask):
    print("\n==================================================================")
    print("      CISCO CCNA // 4-WAY MASK & BIT CONVERTER                    ")
    print("==================================================================")
    
    try:
        if "." in prefix_or_mask:
            net = ipaddress.IPv4Network(f"0.0.0.0/{prefix_or_mask}", strict=False)
        else:
            prefix = prefix_or_mask.replace("/", "")
            net = ipaddress.IPv4Network(f"0.0.0.0/{prefix}", strict=False)
    except ValueError as e:
        print(f"[!] Input Error: {e}")
        print("==================================================================\n")
        return

    cidr = f"/{net.prefixlen}"
    netmask = str(net.netmask)
    wildcard = str(net.hostmask)
    
    binary_octets = [f"{int(o):08b}" for o in netmask.split(".")]
    binary_mask = ".".join(binary_octets)
    total_hosts = net.num_addresses - 2 if net.num_addresses > 2 else 0

    print(f" Input Query        : {prefix_or_mask}")
    print("------------------------------------------------------------------")
    print(f" [1] CIDR Prefix    : {cidr}")
    print(f" [2] Subnet Mask    : {netmask}")
    print(f" [3] Wildcard Mask  : {wildcard}")
    print(f" [4] Binary Mask    : {binary_mask}")
    print("------------------------------------------------------------------")
    print(f" Network Bits (1s)  : {net.prefixlen}")
    print(f" Host Bits (0s)     : {32 - net.prefixlen}")
    print(f" Usable Host Count  : {total_hosts:,}")
    print("==================================================================\n")

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "/24"
    convert_mask(query)
