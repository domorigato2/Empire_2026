# Save as: C:\Users\sheil\Empire_2026\empire_core.py
import os
import subprocess
import sys

MENU = """
====================================================================
           ROOT KERNEL // EMPIRE MASTER INTERFACE 2026
====================================================================
[1] CCNA Cognitive Drills      (ccna_drill.py / ccna_quiz.py)
[2] Cisco Config Generators    (VLAN, DHCP, OSPF, NAT, ACL, PortSec)
[3] Subnetting & IP Engines    (subnet_calc.py / vlsm_calc.py)
[4] Network Recon & Scanners   (port_scanner.py / arp_scout.py)
[5] Cryptography & Vault       (vault_engine.py / crypto_hasher.py)
[6] War Chest & Finance        (war_chest.py / capital_engine.py)
[7] Launch Packet Tracer Lab   (CCNA_ROAS_DHCP_Lab.pkt)
[8] System Telemetry & Streaks (streaks.py / empire_dashboard.py)
[0] Exit Shell
====================================================================
"""

def execute_tool(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if os.path.exists(script_path):
        print(f"\n[*] Booting {script_name}...")
        if script_name.endswith('.pkt'):
            os.startfile(script_path)
        else:
            subprocess.run([sys.executable, script_path])
    else:
        print(f"\n[-] ERROR: Module {script_name} not found in root path.")
    input("\n[Press Enter to return to Master Interface]")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(MENU)
        choice = input("Enter tactical vector [0-8]: ").strip()

        if choice == '1':
            execute_tool("ccna_drill.py")
        elif choice == '2':
            print("\n--- Cisco Generator Sub-Vector ---")
            print("1. VLAN Builder  2. Trunk Gen  3. DHCP Gen  4. OSPF Gen  5. ACL Gen  6. NAT Gen")
            sub = input("Select: ").strip()
            mapping = {
                "1": "cisco_vlan_builder.py", "2": "cisco_trunk_gen.py", 
                "3": "cisco_dhcp_gen.py", "4": "cisco_ospf_gen.py", 
                "5": "cisco_acl_gen.py", "6": "cisco_nat_gen.py"
            }
            if sub in mapping:
                execute_tool(mapping[sub])
        elif choice == '3':
            execute_tool("subnet_calc.py")
        elif choice == '4':
            execute_tool("port_range_scanner.py")
        elif choice == '5':
            execute_tool("vault_engine.py")
        elif choice == '6':
            execute_tool("war_chest.py")
        elif choice == '7':
            execute_tool("CCNA_ROAS_DHCP_Lab.pkt")
        elif choice == '8':
            execute_tool("empire_dashboard.py")
        elif choice == '0':
            print("\n[*] Terminating Master Interface. Standby.")
            sys.exit(0)
        else:
            print("[-] Invalid packet input.")

if __name__ == "__main__":
    main()