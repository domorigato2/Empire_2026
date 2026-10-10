import ipaddress
import sys

def vlsm_allocate(base_cidr, host_requirements):
    print("\n==================================================================")
    print("     CISCO CCNA // VLSM (VARIABLE LENGTH SUBNET MASK) ENGINE      ")
    print("==================================================================")
    print(f" Base Network : {base_cidr}")
    print(f" Host Demands : {host_requirements}")
    print("------------------------------------------------------------------")

    try:
        base_net = ipaddress.ip_network(base_cidr, strict=False)
    except ValueError as e:
        print(f"[!] Invalid Base Network: {e}")
        return

    # Sort host requirements descending (allocate largest subnets first)
    sorted_hosts = sorted(host_requirements, reverse=True)
    current_net = base_net

    for idx, hosts in enumerate(sorted_hosts, 1):
        # Need hosts + 2 addresses (Network ID + Broadcast)
        needed_ips = hosts + 2
        bits = 0
        while (2 ** bits) < needed_ips:
            bits += 1
        prefix = 32 - bits
        
        try:
            subnets = list(current_net.subnets(new_prefix=prefix))
            allocated = subnets[0]
            current_net = subnets[1] if len(subnets) > 1 else None
            
            print(f" [Subnet {idx:02d}] Req: {hosts:>4} hosts --> Assigned: {allocated} | Usable: {allocated.num_addresses - 2}")
        except Exception as e:
            print(f" [Subnet {idx:02d}] Allocation Failed for {hosts} hosts: {e}")
            break

    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        base = sys.argv[1]
        requirements = [int(x) for x in sys.argv[2:]]
        vlsm_allocate(base, requirements)
    else:
        print("[!] Usage: python vlsm_calc.py <BASE_CIDR> <HOST_REQ_1> <HOST_REQ_2> ...")
        print("    Example: python vlsm_calc.py 192.168.100.0/24 50 20 10 2")
