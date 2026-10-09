import socket
import sys

PORTS = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT"
}

def scan_target(target_host):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"\n[!] Resolution Error: Unable to resolve '{target_host}'.\n")
        return

    print("\n==================================================")
    print("      TACTICAL PORT SCANNER // SOCKET PROBE       ")
    print("==================================================")
    print(f" Target Host : {target_host}")
    print(f" Target IP   : {target_ip}")
    print(" Probing Ports: 21, 22, 53, 80, 443, 8080")
    print("--------------------------------------------------")

    for port, service in PORTS.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.7)  # 700ms probe window
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f" [+] PORT {port:04d} [{service:<8}] --> OPEN / LISTENING")
        else:
            print(f" [-] PORT {port:04d} [{service:<8}] --> CLOSED / FILTERED")
        s.close()
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan_target(sys.argv[1])
    else:
        print("[!] Usage: python port_scanner.py <HOST_OR_IP>")
