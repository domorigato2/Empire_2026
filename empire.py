import subprocess
import sys

def main():
    while True:
        print("\n=========================================")
        print("        DOMINIC EMPIRE OS v3.1           ")
        print("=========================================")
        print(" [1]  Log Telemetry (Beers, Cigs, Day 17)")
        print(" [2]  War Chest Engine ($1,000 Target)   ")
        print(" [3]  View Raw Telemetry Vault (cat)     ")
        print(" [4]  Run CCNA Network Reachability Probe")
        print(" [5]  Run CCNA IPv4 Subnet Calculator    ")
        print(" [6]  View Operational Streak Vault      ")
        print(" [7]  Run CCNA Terminal Drill Engine     ")
        print(" [8]  Run CCNA Layer 4 TCP Port Scanner  ")
        print(" [9]  Run CCNA DNS Forward/Reverse Lookup")
        print(" [10] Run CCNA IPv4 Binary Converter     ")
        print(" [11] Run CCNA Subnet Speed Drill        ")
        print(" [12] Run Vault Telemetry Stats Parser   ")
        print(" [13] Run Cisco IOS VLAN Config Builder  ")
        print(" [14] Run CCNA MAC Address Formatter     ")
        print(" [15] Run CCNA Security Hash Generator   ")
        print(" [16] Exit Terminal                      ")
        print("=========================================")
        
        choice = input("Select Subsystem [1-16]: ")
        
        if choice == '1':
            subprocess.run([sys.executable, "empire_log.py"])
        elif choice == '2':
            subprocess.run([sys.executable, "war_chest.py"])
        elif choice == '3':
            try:
                with open("telemetry_vault.txt", "r") as file:
                    print("\n--- VAULT ARCHIVE ---")
                    print(file.read())
                    print("---------------------")
            except FileNotFoundError:
                print("\n[!] No vault data found yet.")
        elif choice == '4':
            subprocess.run([sys.executable, "net_probe.py"])
        elif choice == '5':
            subprocess.run([sys.executable, "subnet_calc.py"])
        elif choice == '6':
            subprocess.run([sys.executable, "streaks.py"])
        elif choice == '7':
            subprocess.run([sys.executable, "ccna_quiz.py"])
        elif choice == '8':
            subprocess.run([sys.executable, "port_scanner.py"])
        elif choice == '9':
            subprocess.run([sys.executable, "dns_tool.py"])
        elif choice == '10':
            subprocess.run([sys.executable, "binary_calc.py"])
        elif choice == '11':
            subprocess.run([sys.executable, "subnet_drill.py"])
        elif choice == '12':
            subprocess.run([sys.executable, "vault_stats.py"])
        elif choice == '13':
            subprocess.run([sys.executable, "cisco_vlan_builder.py"])
        elif choice == '14':
            subprocess.run([sys.executable, "mac_formatter.py"])
        elif choice == '15':
            subprocess.run([sys.executable, "hash_maker.py"])
        elif choice == '16':
            print("\nShutting down Empire console. Hold the line.")
            break
        else:
            print("\n[!] Invalid command. Select 1 through 16.")

if __name__ == "__main__":
    main()