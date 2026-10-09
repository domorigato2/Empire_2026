import sys

def generate_cisco_config(hostname, vlan_id, vlan_name, ip_addr, subnet_mask):
    print("\n==================================================")
    print("     CISCO IOS // AUTOMATED CONFIG GENERATOR      ")
    print("==================================================")
    config = f"""! --- [CISCO IOS CONFIG PAYLOAD: {hostname}] ---
enable
configure terminal
hostname {hostname}
!
vlan {vlan_id}
 name {vlan_name}
exit
!
interface Vlan{vlan_id}
 description SVI Gateway for {vlan_name}
 ip address {ip_addr} {subnet_mask}
 no shutdown
exit
!
line vty 0 4
 transport input ssh
 login local
exit
!
end
write memory
! --- [END PAYLOAD] ---"""
    print(config)
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 6:
        h_name = sys.argv[1]
        v_id = sys.argv[2]
        v_name = sys.argv[3]
        ip = sys.argv[4]
        mask = sys.argv[5]
        generate_cisco_config(h_name, v_id, v_name, ip, mask)
    else:
        print("[!] Usage: python cisco_gen.py <HOSTNAME> <VLAN_ID> <VLAN_NAME> <SVI_IP> <SUBNET_MASK>")
        print("    Example: python cisco_gen.py SW1-CORE 20 SERVERS 10.20.0.1 255.255.255.0")
