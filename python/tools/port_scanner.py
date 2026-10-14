import socket

# Dynamic User Input:
target = input("\nEnter target IP address to scan (e.g. 192.168.1.1): ").strip()

# Common router & infrastructure service ports:
ports = [21, 22, 23, 53, 80, 135, 139, 443, 445, 8080]

print(f"\n[*] Probing perimeter defenses on: {target}")
print("=" * 55)

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.7)  # 700ms timeout for network latency
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] Port {port:<5} | OPEN      | Service Active")
    else:
        print(f"[-] Port {port:<5} | Closed    | Refused / Filtered")
        
    s.close()

print("=" * 55)
print("[*] Reconnaissance complete.\n")