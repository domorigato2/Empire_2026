import sys

def generate_cisco_dhcp(pool_name, network_id, subnet_mask, default_router, dns_server="8.8.8.8", domain_name="empire.local"):
    net_parts = network_id.split(".")
    base_prefix = ".".join(net_parts[:3])
    start_exclude = f"{base_prefix}.1"
    end_exclude = f"{base_prefix}.10"

    print("\n==================================================================")
    print("     CISCO CCNA // AUTOMATED DHCP SERVER POOL GENERATOR           ")
    print("==================================================================")
    config = f"""! =======================================================
! CISCO IOS DHCP POOL CONFIGURATION (Paste into Cisco Router)
! =======================================================
enable
configure terminal
!
! Reserve static infrastructure addresses (Gateway, Switches, Servers)
ip dhcp excluded-address {start_exclude} {end_exclude}
!
ip dhcp pool {pool_name}
 network {network_id} {subnet_mask}
 default-router {default_router}
 dns-server {dns_server}
 domain-name {domain_name}
 lease 7
exit
end
write memory
! =======================================================
! Operational Verification:
! show ip dhcp pool
! show ip dhcp binding
! ======================================================="""
    print(config)
    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        p_name = sys.argv[1]
        net = sys.argv[2]
        mask = sys.argv[3]
        gw = sys.argv[4]
        dns = sys.argv[5] if len(sys.argv) > 5 else "8.8.8.8"
        generate_cisco_dhcp(p_name, net, mask, gw, dns)
    else:
        print("[!] Usage: python cisco_dhcp_gen.py <POOL_NAME> <NETWORK_ID> <SUBNET_MASK> <DEFAULT_ROUTER> [DNS_SERVER]")
        print("    Example: python cisco_dhcp_gen.py VLAN20_POOL 10.20.0.0 255.255.255.0 10.20.0.1 8.8.8.8")
