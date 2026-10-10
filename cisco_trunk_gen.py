import sys

def generate_roas(router_int, switch_trunk_int, vlan_id, vlan_name, gateway_ip, subnet_mask):
    print("\n==================================================================")
    print("     CISCO CCNA // 802.1Q INTER-VLAN ROUTING ARCHITECT            ")
    print("==================================================================")
    
    config = f"""! =======================================================
! [1] SWITCH TRUNK CONFIGURATION (Paste into Cisco Switch)
! =======================================================
enable
configure terminal
vlan {vlan_id}
 name {vlan_name}
exit
interface {switch_trunk_int}
 description 802.1Q Trunk Link to Router {router_int}
 switchport mode trunk
 switchport trunk allowed vlan add {vlan_id}
 no shutdown
exit
end

! =======================================================
! [2] ROUTER-ON-A-STICK SUBINTERFACE (Paste into Cisco Router)
! =======================================================
enable
configure terminal
interface {router_int}
 no shutdown
exit
interface {router_int}.{vlan_id}
 description Gateway for VLAN {vlan_id} ({vlan_name})
 encapsulation dot1Q {vlan_id}
 ip address {gateway_ip} {subnet_mask}
 no shutdown
exit
end"""
    print(config)
    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 7:
        r_int = sys.argv[1]
        sw_int = sys.argv[2]
        v_id = sys.argv[3]
        v_name = sys.argv[4]
        gw = sys.argv[5]
        mask = sys.argv[6]
        generate_roas(r_int, sw_int, v_id, v_name, gw, mask)
    else:
        print("[!] Usage: python cisco_trunk_gen.py <ROUTER_INT> <SWITCH_INT> <VLAN_ID> <VLAN_NAME> <GATEWAY_IP> <SUBNET_MASK>")
        print("    Example: python cisco_trunk_gen.py G0/0/0 Fa0/24 20 SALES 192.168.20.1 255.255.255.0")
