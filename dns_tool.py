import socket

print("=========================================")
print("      CCNA DNS FORWARD/REVERSE LOOKUP    ")
print("=========================================")

target = input("Enter Domain Name or IP (e.g., google.com or 8.8.8.8): ").strip()

try:
    # Check if input is IP or Domain
    if target.replace(".", "").isdigit():
        # Reverse DNS Lookup (IP -> Hostname)
        hostname, _, _ = socket.gethostbyaddr(target)
        print("-----------------------------------------")
        print(f"QUERY TYPE : REVERSE DNS (PTR)")
        print(f"IP ADDRESS : {target}")
        print(f"HOSTNAME   : {hostname}")
        print("-----------------------------------------")
    else:
        # Forward DNS Lookup (Domain -> IP)
        ip_addr = socket.gethostbyname(target)
        print("-----------------------------------------")
        print(f"QUERY TYPE : FORWARD DNS (A RECORD)")
        print(f"DOMAIN     : {target}")
        print(f"IP ADDRESS : {ip_addr}")
        print("-----------------------------------------")
        
    print("[✓] RESOLUTION SUCCESSFUL. LAYER 7 OPERATIONAL.")

except socket.herror as err:
    print(f"\n[!] Reverse DNS lookup failed: {err}")
except socket.gaierror as err:
    print(f"\n[!] Forward DNS resolution failed: {err}")

print("=========================================")