import socket
import sys

def dns_lookup(target):
    print("\n==================================================")
    print("      TACTICAL DNS RECON // RESOLUTION ENGINE     ")
    print("==================================================")
    print(f" Target Query : {target}")
    print(" Interrogating DNS Resolvers...")
    print("--------------------------------------------------")

    # Reverse DNS check (PTR) if target starts with numbers
    if any(char.isdigit() for char in target.split(".")[0]):
        try:
            hostname, aliases, ips = socket.gethostbyaddr(target)
            print(f" [RECORD TYPE] Reverse DNS (PTR)")
            print(f" [HOSTNAME   ] {hostname}")
            if aliases:
                print(f" [ALIASES    ] {', '.join(aliases)}")
            print(f" [ASSOCIATED ] {', '.join(ips)}")
            print("--------------------------------------------------")
        except socket.herror:
            print(" [-] Reverse DNS (PTR): No PTR record found.")
            print("--------------------------------------------------")

    # Forward DNS check (A-Records / CNAMEs)
    try:
        host, aliases, ip_list = socket.gethostbyname_ex(target)
        print(f" [RECORD TYPE] Forward DNS (A-Records)")
        print(f" [CANONICAL  ] {host}")
        if aliases:
            print(f" [CNAMEs     ] {', '.join(aliases)}")
        print(f" [A-RECORDS  ] Resolved IP Endpoints ({len(ip_list)} total):")
        for idx, ip in enumerate(ip_list, 1):
            print(f"    --> Node {idx:02d}: {ip}")
    except socket.gaierror as e:
        print(f"[!] Forward Resolution Failed: {e}")
    except Exception as e:
        print(f"[!] Extraction Error: {e}")

    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dns_lookup(sys.argv[1])
    else:
        print("[!] Usage: python dns_scout.py <DOMAIN_OR_IP>")
