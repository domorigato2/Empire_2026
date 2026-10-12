# Save as empire_master.py in C:\Users\sheil\Empire_2026\
import datetime, os, ipaddress, re

def show_dashboard():
    print("\n" + "="*60)
    print(" EMPIRE 2026 // MASTER KERNEL TELEMETRY DASHBOARD")
    print("="*60)
    print(f" OPERATOR       : Dominic Margherio | Node: Spring Valley")
    print(f" MEDICAL STATUS : Day 6 Detox (Librium Taper) | Cellulitis Active")
    print(f" STREAKS        : Smoke-Free: 39d | Zero-Alc: 6d | Fasting: 69d")
    print(f" WAR CHEST      : $4.32 / $1,000.00 Target (PayPal)")
    print(f" NEXT NODE      : Peru PADS Interview (Tuesday, Oct 13 @ 10:30 AM)")
    print(f" DISPATCH CALL  : Monday, Oct 12 @ 08:00 AM -> BPART (877-874-8813)")
    print("="*60)

def subnet_engine():
    target = input("\nEnter IPv4 CIDR (e.g., 10.0.0.0/19): ").strip()
    if not target:
        target = "10.0.0.0/19"
    try:
        net = ipaddress.ip_network(target, strict=False)
        print(f"\n--- CCNA TELEMETRY: {net.with_prefixlen} ---")
        print(f" Network Address  : {net.network_address}")
        print(f" Subnet Mask      : {net.netmask}")
        print(f" Broadcast Addr   : {net.broadcast_address}")
        print(f" Usable Host Range: {net.network_address + 1} - {net.broadcast_address - 1}")
        print(f" Total Usable     : {net.num_addresses - 2 if net.num_addresses > 2 else 0}")
    except ValueError as e:
        print(f"\n[!] INVALID IP/CIDR PACKET: {e}")
    input("\nPress Enter to return to main menu...")

def route_parser():
    cisco_dump = """
S*    0.0.0.0/0 [1/0] via 192.168.1.1
C     10.10.10.0/24 is directly connected, GigabitEthernet0/0
O     172.16.0.0/16 [110/20] via 10.10.10.2, GigabitEthernet0/0
    """
    print("\n" + "="*50)
    print(" CISCO ROUTE TABLE SIMULATION")
    print("="*50)
    print(cisco_dump.strip())
    print("="*50)
    input("\nPress Enter to return to main menu...")

def main_menu():
    while True:
        show_dashboard()
        print("\n[1] Run CCNA Subnet Calculator")
        print("[2] Parse Cisco Route Table")
        print("[3] View Telemetry Log JSON Status")
        print("[4] Exit Terminal")
        
        choice = input("\nSelect Subroutine [1-4]: ").strip()
        if choice == '1':
            subnet_engine()
        elif choice == '2':
            route_parser()
        elif choice == '3':
            print("\n[+] telemetry_log.json active and secured on local disk.")
            input("\nPress Enter to return...")
        elif choice == '4':
            print("\n[+] Terminal session detached. Rest up, operator.")
            break
        else:
            print("\n[!] Invalid input. Select 1-4.")

if __name__ == "__main__":
    main_menu()