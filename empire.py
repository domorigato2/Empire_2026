import subprocess
import sys

def main():
    while True:
        print("\n=========================================")
        print("        DOMINIC EMPIRE OS v2.1           ")
        print("=========================================")
        print(" [1] Log Telemetry (Beers, Cigs, Day 15) ")
        print(" [2] War Chest Engine ($1,000 Target)    ")
        print(" [3] View Past Telemetry Vault           ")
        print(" [4] Run CCNA Network Reachability Probe ")
        print(" [5] Run CCNA IPv4 Subnet Calculator     ")
        print(" [6] Exit Terminal                       ")
        print("=========================================")
        
        choice = input("Select Subsystem [1-6]: ")
        
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
            print("\nShutting down Empire console. Hold the line.")
            break
        else:
            print("\n[!] Invalid command. Select 1 through 6.")

if __name__ == "__main__":
    main()