import socket
import sys

def send_payload(message="Hello from Empire Client core."):
    print("\n==================================================")
    print("      TCP SOCKET CLIENT // TEST SENDER            ")
    print("==================================================")
    print(f" Connecting to 127.0.0.1:9999...")
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 9999))
        print(" [+] Handshake complete. Sending payload...")
        
        s.sendall((message + "\n").encode('utf-8'))
        
        response = s.recv(1024).decode('utf-8')
        print(f" [+] Server Response: {response.strip()}")
        s.close()
        print("--------------------------------------------------")
        print(" Client Session Terminated Successfully.")
        print("==================================================\n")
    except Exception as e:
        print(f"[!] Connection Failed: {e}")

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello from Empire Client core."
    send_payload(msg)
