import socket
import sys

def start_listener(port=9999):
    print("\n==================================================")
    print("      TCP SOCKET LISTENER // TEST SERVER          ")
    print("==================================================")
    print(f" Binding to localhost on port {port}...")
    print(" Waiting for incoming TCP handshake (Press Ctrl+C to stop)...")
    print("--------------------------------------------------")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        s.bind(("127.0.0.1", port))
        s.listen(1)
        conn, addr = s.accept()
        print(f" [+] Connection established with client: {addr}")
        
        data = conn.recv(1024).decode('utf-8')
        print(f" [+] Received Payload: {data.strip()}")
        
        conn.sendall(b"ACK: Payload received by Empire Core Server.\n")
        conn.close()
        s.close()
        print("--------------------------------------------------")
        print(" Listener Session Terminated Successfully.")
        print("==================================================\n")
    except Exception as e:
        print(f"[!] Listener Error: {e}")

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
    start_listener(p)
