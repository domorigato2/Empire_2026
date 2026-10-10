import sys

def generate_static_route(dest_net, dest_mask, next_hop="", exit_int="", ad=""):
    print("\n==================================================================")
    print("     CISCO CCNA // STATIC & FLOATING ROUTE ARCHITECT              ")
    print("==================================================================")

    config = "! =======================================================\n"
    config += "! CISCO IOS STATIC ROUTING PAYLOAD\n"
    config += "! =======================================================\n"
    config += "enable\nconfigure terminal\n!\n"

    target_clause = f"{next_hop} {exit_int}".strip() if next_hop or exit_int else "<NEXT_HOP_OR_INTERFACE>"
    ad_clause = f" {ad}" if ad else ""

    is_default = (dest_net == "0.0.0.0" and dest_mask == "0.0.0.0") or dest_net.lower() == "default"

    if is_default:
        config += f"ip route 0.0.0.0 0.0.0.0 {target_clause}{ad_clause}\n"
        route_type = "Default Static Route (Gateway of Last Resort)"
    else:
        config += f"ip route {dest_net} {dest_mask} {target_clause}{ad_clause}\n"
        route_type = "Standard / Floating Static Route"

    config += "!\nend\nwrite memory\n!\n"
    config += "! Operational Verification:\n"
    config += "! show ip route static\n"
    config += "! show ip route 0.0.0.0"

    print(f" Route Profile : {route_type}")
    if ad:
        print(f" Floating AD   : {ad} (Backs up dynamic protocols with lower AD)")
    print("------------------------------------------------------------------")
    print(config)
    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        d_net = sys.argv[1]
        d_mask = sys.argv[2]
        hop = sys.argv[3] if len(sys.argv) > 3 else ""
        intf = sys.argv[4] if len(sys.argv) > 4 else ""
        admin_dist = sys.argv[5] if len(sys.argv) > 5 else ""
        generate_static_route(d_net, d_mask, hop, intf, admin_dist)
    else:
        print("[!] Usage:")
        print("    Default:  python cisco_static_route_gen.py 0.0.0.0 0.0.0.0 209.165.200.226")
        print("    Floating: python cisco_static_route_gen.py 10.20.0.0 255.255.255.0 192.168.1.2 '' 200")
