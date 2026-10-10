import os
import sys
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_mod(script_name, *args):
    cmd = [sys.executable, script_name] + list(args)
    subprocess.run(cmd)
    input("\n[Press Enter to return to Master Console...]")

def menu():
    while True:
        clear()
        print("==================================================================")
        print("        DOMINIC EMPIRE // MASTER ARSENAL CONSOLE v2.2             ")
        print("==================================================================")
        print(" [DIVISION 1: CHASSIS & LOGISTICS]")
        print("   [1]  Empire Telemetry HUD (empire_dashboard.py)")
        print("   [2]  Append Telemetry Log (empire_logger.py)")
        print("   [3]  Automated Directory Cleaner (cleaner.py)")
        print("   [4]  Process Hunter (process_hunter.py)")
        print("   [5]  Active Socket Scout (netstat_scout.py)")
        print("   [6]  Recursive CLI Grep Search (file_search.py)")
        print("\n [DIVISION 2: NETWORK RECONNAISSANCE & NMS]")
        print("   [7]  ICMP Ping Reachability Scout (ping_scout.py)")
        print("   [8]  Layer 3 Jitter & PDV Analyzer (jitter_scout.py)")
        print("   [9]  Traceroute Route Hop Scout (hop_scout.py)")
        print("   [10] TCP Socket Port Scanner (port_scanner.py)")
        print("   [11] Multi-Threaded Port Range Sweeper (port_range_scanner.py)")
        print("   [12] Multi-Threaded LAN Sweeper (lan_sweeper.py)")
        print("   [13] Subnet Live Host Pinger (subnet_pinger.py)")
        print("   [14] Layer 7 DNS Recon Engine (dns_scout.py)")
        print("   [15] Batch Reverse DNS IP Resolver (ip_resolver.py)")
        print("   [16] Layer 2 ARP Table Inspector (arp_scout.py)")
        print("   [17] HTTP Service Banner Grabber (banner_grab.py)")
        print("   [18] Continuous Uptime Heartbeat Monitor (uptime_monitor.py)")
        print("   [19] Automated Reconnaissance Pipeline (quick_recon.py)")
        print("   [20] JSON Recon Report Serializer (recon_report.py)")
        print("   [21] Automated NMS Config Backup Engine (config_backup_sim.py)")
        print("\n [DIVISION 3: CISCO CCNA AUTOMATION & PARSING]")
        print("   [22] Subnet & CIDR Architect (subnet_calc.py)")
        print("   [23] 4-Way Mask & Bit Converter (mask_converter.py)")
        print("   [24] Subnet Host Range Exporter (subnet_export.py)")
        print("   [25] Cisco SVI Switchport Gen (cisco_gen.py)")
        print("   [26] Cisco 802.1Q ROAS Trunk Gen (cisco_trunk_gen.py)")
        print("   [27] Cisco DHCP Server Pool Gen (cisco_dhcp_gen.py)")
        print("   [28] Cisco Standard & Extended ACL Gen (cisco_acl_gen.py)")
        print("   [29] Cisco Static & Floating Route Gen (cisco_static_route_gen.py)")
        print("   [30] Cisco NAT/PAT Overload Gen (cisco_nat_gen.py)")
        print("   [31] Cisco OSPFv2 Routing Gen (cisco_ospf_gen.py)")
        print("   [32] Cisco Config Regex Interface Extractor (config_parser.py)")
        print("\n [DIVISION 4: CRYPTO & DRILLS]")
        print("   [33] CCNA 200-301 Exam Quiz Drill (ccna_drill.py)")
        print("   [34] Caesar Cipher Engine (cipher.py)")
        print("   [35] Brute-Force Cipher Breaker (crack.py)")
        print("   [36] Cryptographic Hash Generator (crypto_hasher.py)")
        print("   [37] Secure Key / Password Gen (gen_pass.py)")
        print("   [38] Bingo Clash Ticket ROI Calc (bingo_calc.py)")
        print("\n   [0]  Terminate Master Console")
        print("==================================================================")
        choice = input(" [>] Select Module: ").strip()

        if choice == "1":
            run_mod("empire_dashboard.py")
        elif choice == "2":
            entry = input(" Enter telemetry log text: ")
            run_mod("empire_logger.py", entry)
        elif choice == "3":
            run_mod("cleaner.py")
        elif choice == "4":
            run_mod("process_hunter.py")
        elif choice == "5":
            run_mod("netstat_scout.py")
        elif choice == "6":
            run_mod("file_search.py", "def")
        elif choice == "7":
            t = input(" Enter target to ping (default 1.1.1.1): ") or "1.1.1.1"
            run_mod("ping_scout.py", t)
        elif choice == "8":
            t = input(" Enter target for jitter test (default 1.1.1.1): ") or "1.1.1.1"
            run_mod("jitter_scout.py", t, "10")
        elif choice == "9":
            t = input(" Enter target for traceroute (default 1.1.1.1): ") or "1.1.1.1"
            run_mod("hop_scout.py", t, "10")
        elif choice == "10":
            t = input(" Enter target host to scan (default 127.0.0.1): ") or "127.0.0.1"
            run_mod("port_scanner.py", t)
        elif choice == "11":
            t = input(" Enter host to range scan (default 127.0.0.1): ") or "127.0.0.1"
            run_mod("port_range_scanner.py", t, "1", "100")
        elif choice == "12":
            sub = input(" Base subnet (default 192.168.1): ") or "192.168.1"
            run_mod("lan_sweeper.py", sub, "100", "120")
        elif choice == "13":
            sub = input(" Enter target CIDR to ping sweep (default 192.168.1.0/28): ") or "192.168.1.0/28"
            run_mod("subnet_pinger.py", sub)
        elif choice == "14":
            t = input(" Enter domain or IP to resolve: ") or "cisco.com"
            run_mod("dns_scout.py", t)
        elif choice == "15":
            ips = input(" Enter IPs separated by space: ") or "8.8.8.8 1.1.1.1"
            run_mod("ip_resolver.py", *ips.split())
        elif choice == "16":
            run_mod("arp_scout.py")
        elif choice == "17":
            t = input(" Enter target IP (default 192.168.1.1): ") or "192.168.1.1"
            run_mod("banner_grab.py", t)
        elif choice == "18":
            t = input(" Enter target to monitor (default 1.1.1.1): ") or "1.1.1.1"
            run_mod("uptime_monitor.py", t, "3")
        elif choice == "19":
            t = input(" Enter target for recon pipeline (default 127.0.0.1): ") or "127.0.0.1"
            run_mod("quick_recon.py", t)
        elif choice == "20":
            t = input(" Enter target for JSON report (default 1.1.1.1): ") or "1.1.1.1"
            run_mod("recon_report.py", t)
        elif choice == "21":
            run_mod("config_backup_sim.py")
        elif choice == "22":
            c = input(" Enter CIDR (e.g. 192.168.10.0/24): ") or "192.168.10.0/24"
            run_mod("subnet_calc.py", c)
        elif choice == "23":
            m = input(" Enter mask or CIDR to convert (e.g. /28): ") or "/28"
            run_mod("mask_converter.py", m)
        elif choice == "24":
            c = input(" Enter CIDR to map (e.g. 10.0.0.0/28): ") or "10.0.0.0/28"
            run_mod("subnet_export.py", c)
        elif choice == "25":
            run_mod("cisco_gen.py", "SW-CORE", "10", "MGMT", "192.168.10.1", "255.255.255.0")
        elif choice == "26":
            run_mod("cisco_trunk_gen.py", "G0/0/0", "Fa0/24", "20", "DATA", "10.20.0.1", "255.255.255.0")
        elif choice == "27":
            run_mod("cisco_dhcp_gen.py", "POOL_DATA", "10.20.0.0", "255.255.255.0", "10.20.0.1", "8.8.8.8")
        elif choice == "28":
            run_mod("cisco_acl_gen.py", "standard", "10", "permit", "192.168.10.0", "0.0.0.255")
        elif choice == "29":
            run_mod("cisco_static_route_gen.py", "0.0.0.0", "0.0.0.0", "209.165.200.226")
        elif choice == "30":
            run_mod("cisco_nat_gen.py", "192.168.10.0", "0.0.0.255", "G0/0/0", "G0/0/1", "1")
        elif choice == "31":
            run_mod("cisco_ospf_gen.py", "1", "1.1.1.1", "0", "G0/0/0")
        elif choice == "32":
            run_mod("config_parser.py", "mock_config.txt")
        elif choice == "33":
            run_mod("ccna_drill.py")
        elif choice == "34":
            run_mod("cipher.py", "encrypt", "3", "Dominic Margherio")
        elif choice == "35":
            run_mod("crack.py", "Grplqlf Pdujkhulr")
        elif choice == "36":
            run_mod("crypto_hasher.py", "DominicEmpire2026")
        elif choice == "37":
            run_mod("gen_pass.py", "24")
        elif choice == "38":
            run_mod("bingo_calc.py", "9300")
        elif choice == "0":
            print("\n[!] Exiting Master Arsenal Console.")
            break

if __name__ == "__main__":
    menu()
