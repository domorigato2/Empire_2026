import socket
import sys

def resolve_ips(ip_list):
    print("\n==================================================")
    print("      REVERSE DNS // BATCH IP RESOLVER            ")
    print("==================================================")
    print(f" Processing {len(ip_list)} target IP addresses...")
    print("--------------------------------------------------")

    for ip in ip_list:
        ip = ip.strip()
        if not ip:
            continue
        try:
            hostname, aliases, _ = socket.gethostbyaddr(ip)
            print(f" [+] {ip:<15} --> {hostname}")
        except socket.herror:
            print(f" [-] {ip:<15} --> [NO PTR RECORD FOUND]")
        except Exception as e:
            print(f" [!] {ip:<15} --> Error: {e}")

    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        targets = sys.argv[1:]
        resolve_ips(targets)
    else:
        print("[!] Usage: python ip_resolver.py <IP_1> <IP_2> <IP_3> ...")
        print("    Example: python ip_resolver.py 8.8.8.8 1.1.1.1 192.168.1.1")
