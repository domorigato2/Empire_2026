import sys

def generate_ospf(process_id, router_id, area_id, networks, active_interface):
    print("\n==================================================================")
    print("     CISCO CCNA // OSPFv2 LINK-STATE ROUTING ARCHITECT            ")
    print("==================================================================")
    
    config = "! =======================================================\n"
    config += f"! CISCO IOS OSPF PROCESS #{process_id} CONFIGURATION\n"
    config += "! =======================================================\n"
    config += "enable\nconfigure terminal\n!\n"
    config += f"router ospf {process_id}\n"
    config += f" router-id {router_id}\n"
    
    for net, wildcard in networks:
        config += f" network {net} {wildcard} area {area_id}\n"
        
    config += " !\n ! Harden LAN ports: suppress OSPF Hellos on non-router links\n"
    config += " passive-interface default\n"
    config += f" no passive-interface {active_interface}\n"
    config += "exit\nend\nwrite memory\n!\n"
    config += "! Operational Verification:\n"
    config += "! show ip protocols\n"
    config += "! show ip ospf neighbor\n"
    config += "! show ip route ospf"
    
    print(config)
    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        pid = sys.argv[1]
        rid = sys.argv[2]
        aid = sys.argv[3]
        active_int = sys.argv[4]
        # Example network pairs passed as net1 wild1 net2 wild2
        net_args = sys.argv[5:]
        net_pairs = []
        for i in range(0, len(net_args), 2):
            if i + 1 < len(net_args):
                net_pairs.append((net_args[i], net_args[i+1]))
        if not net_pairs:
            net_pairs = [("10.20.0.0", "0.0.0.255"), ("192.168.10.0", "0.0.0.255")]
            
        generate_ospf(pid, rid, aid, net_pairs, active_int)
    else:
        print("[!] Usage: python cisco_ospf_gen.py <PROCESS_ID> <ROUTER_ID> <AREA_ID> <ACTIVE_ROUTER_INT> [NET1 WILD1 NET2 WILD2...]")
        print("    Example: python cisco_ospf_gen.py 1 1.1.1.1 0 G0/0/0 10.20.0.0 0.0.0.255 192.168.10.0 0.0.0.255")
