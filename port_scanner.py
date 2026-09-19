import socket
import sys

# Standard CCNA Layer 4 Well-Known Ports
TARGET_PORTS = {
    21: "FTP (File Transfer)",
    22: "SSH (Secure Shell)",
    23: "Telnet (Unencrypted CLI)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Web Plaintext)",
    443: "HTTPS (Web Encrypted)",
    8080: "HTTP Alternate / Web Proxy"
}

def scan_target():
    print("=========================================")
    print("      CCNA LAYER 4 TCP PORT SCANNER      ")
    print("=========================================")
    
    target = input("Enter Target IP (Default router: 192.168.1.1): ").strip()
    if not target:
        target = "192.168.1.1"

    print(f"\n[*] Initiating TCP 3-Way Handshake probes on: {target}")
    print("-----------------------------------------")

    for port, service in TARGET_PORTS.items():
        # AF_INET = IPv4, SOCK_STREAM = TCP Handshake
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)  # 600ms timeout for speed
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f" [✓] PORT {port:<5} [{service:<26}] : OPEN (SYN-ACK Received)")
        else:
            print(f" [ ] PORT {port:<5} [{service:<26}] : CLOSED / FILTERED")
            
        s.close()

    print("-----------------------------------------")
    print("SCAN COMPLETE. TRANSPORT LAYER VERIFIED.")
    print("=========================================")

if __name__ == "__main__":
    scan_target()