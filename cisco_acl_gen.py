import sys

def generate_acl(acl_type, acl_number, action, source_net, source_wildcard, dest_net="any", dest_wildcard="", port=""):
    print("\n==================================================================")
    print("     CISCO CCNA // AUTOMATED ACCESS CONTROL LIST (ACL) GEN        ")
    print("==================================================================")
    
    acl_type = acl_type.lower()
    action = action.lower()
    
    config = "! =======================================================\n"
    config += f"! CISCO IOS {acl_type.upper()} ACL #{acl_number} CONFIGURATION\n"
    config += "! =======================================================\n"
    config += "enable\nconfigure terminal\n!\n"
    
    if acl_type == "standard":
        # Standard ACL (Source IP only)
        config += f"access-list {acl_number} {action} {source_net} {source_wildcard}\n"
        config += f"access-list {acl_number} deny any\n!\n"
        config += "! Application to VTY Lines (SSH Hardening):\n"
        config += f"line vty 0 4\n access-class {acl_number} in\nexit\n"
    elif acl_type == "extended":
        # Extended ACL (Protocol, Source, Destination, Port)
        protocol = "tcp" if port else "ip"
        port_clause = f" eq {port}" if port else ""
        dest_clause = f"{dest_net} {dest_wildcard}".strip() if dest_net != "any" else "any"
        config += f"access-list {acl_number} {action} {protocol} {source_net} {source_wildcard} {dest_clause}{port_clause}\n"
        config += f"access-list {acl_number} deny ip any any\n!\n"
        config += "! Application to Physical / SVI Interface:\n"
        config += f"interface <INTERFACE_NAME>\n ip access-group {acl_number} in\nexit\n"
    
    config += "end\nwrite memory\n!\n"
    config += "! Operational Verification:\n"
    config += "! show access-lists"
    
    print(config)
    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        a_type = sys.argv[1]
        a_num = sys.argv[2]
        act = sys.argv[3]
        src = sys.argv[4]
        wild = sys.argv[5] if len(sys.argv) > 5 else "0.0.0.255"
        dst = sys.argv[6] if len(sys.argv) > 6 else "any"
        dst_w = sys.argv[7] if len(sys.argv) > 7 else ""
        p = sys.argv[8] if len(sys.argv) > 8 else ""
        generate_acl(a_type, a_num, act, src, wild, dst, dst_w, p)
    else:
        print("[!] Usage:")
        print("    Standard: python cisco_acl_gen.py standard 10 permit 192.168.10.0 0.0.0.255")
        print("    Extended: python cisco_acl_gen.py extended 101 permit 10.20.0.0 0.0.0.255 any '' 443")
