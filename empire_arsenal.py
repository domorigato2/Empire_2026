import os
import sys
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear()
        print("==========================================================")
        print("     DOMINIC EMPIRE // MASTER ARSENAL CONSOLE v1.0        ")
        print("==========================================================")
        print(" [1] Empire Telemetry HUD (empire_dashboard.py)")
        print(" [2] Append Telemetry Log (empire_logger.py)")
        print(" [3] Subnet & CIDR Architect (subnet_calc.py)")
        print(" [4] TCP Socket Port Scanner (port_scanner.py)")
        print(" [5] ICMP Ping Scout (ping_scout.py)")
        print(" [6] Multi-Threaded LAN Sweeper (lan_sweeper.py)")
        print(" [7] Caesar Cipher Encrypt/Decrypt (cipher.py)")
        print(" [8] Brute-Force Cipher Breaker (crack.py)")
        print(" [9] Cisco IOS Config Generator (cisco_gen.py)")
        print(" [0] Terminate Console")
        print("==========================================================")
        choice = input(" [>] Select Module: ").strip()

        if choice == "1":
            subprocess.run([sys.executable, "empire_dashboard.py"])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "2":
            msg = input(" Enter log text: ")
            subprocess.run([sys.executable, "empire_logger.py", msg])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "3":
            cidr = input(" Enter IP/CIDR (e.g. 192.168.1.0/24): ")
            subprocess.run([sys.executable, "subnet_calc.py", cidr])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "4":
            target = input(" Enter host/IP to scan: ")
            subprocess.run([sys.executable, "port_scanner.py", target])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "5":
            target = input(" Enter host/IP to ping: ")
            subprocess.run([sys.executable, "ping_scout.py", target])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "6":
            subnet = input(" Enter base subnet (default 192.168.1): ") or "192.168.1"
            start = input(" Enter start host (default 100): ") or "100"
            end = input(" Enter end host (default 120): ") or "120"
            subprocess.run([sys.executable, "lan_sweeper.py", subnet, start, end])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "7":
            mode = input(" Mode (encrypt/decrypt): ")
            shift = input(" Shift key (e.g. 3): ")
            text = input(" Text: ")
            subprocess.run([sys.executable, "cipher.py", mode, shift, text])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "8":
            cipher_text = input(" Enter ciphertext to crack: ")
            subprocess.run([sys.executable, "crack.py", cipher_text])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "9":
            h = input(" Hostname: ")
            vid = input(" VLAN ID: ")
            vname = input(" VLAN Name: ")
            ip = input(" SVI IP: ")
            mask = input(" Subnet Mask: ")
            subprocess.run([sys.executable, "cisco_gen.py", h, vid, vname, ip, mask])
            input("\n[Press Enter to return to Arsenal...]")
        elif choice == "0":
            print("\n[!] Exiting Arsenal Console.")
            break

if __name__ == "__main__":
    menu()
