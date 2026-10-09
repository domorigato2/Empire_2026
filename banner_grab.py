import socket
import sys

def grab_banner(ip, port=80):
    print("\n==================================================")
    print("      HTTP BANNER GRABBER // SERVICE FINGERPRINT  ")
    print("==================================================")
    print(f" Target Node : {ip}:{port}")
    print(" Dispatching raw HTTP GET probe...")
    print("--------------------------------------------------")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect((ip, port))
        request = f"GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: EmpireRecon/1.0\r\nConnection: close\r\n\r\n"
        s.send(request.encode())
        response = s.recv(2048).decode(errors="ignore")
        s.close()

        headers = response.split("\r\n\r\n")[0]
        for line in headers.split("\r\n"):
            print(f" [HEADER] {line}")
    except Exception as e:
        print(f"[!] Extraction Failed: {e}")

    print("==================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.100"
    p = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    grab_banner(target, p)
