import socket
import sys
import concurrent.futures
import time

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        result = s.connect_ex((target_ip, port))
        s.close()
        return port, (result == 0)
    except Exception:
        return port, False

def scan_range(target_host, start_port=1, end_port=100):
    print("\n==================================================")
    print("      MULTI-THREADED PORT RANGE SWEEPER           ")
    print("==================================================")
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[!] Resolution Error: Unable to resolve '{target_host}'.")
        return

    print(f" Target Host : {target_host} ({target_ip})")
    print(f" Port Range  : {start_port} -> {end_port}")
    print(" Firing concurrent TCP SYN/CONNECT probes...")
    print("--------------------------------------------------")

    start_time = time.time()
    open_ports = []

    ports = range(start_port, end_port + 1)
    # 50 concurrent worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target_ip, p), ports)
        for port, is_open in results:
            if is_open:
                print(f" [+] PORT {port:05d} --> OPEN / LISTENING")
                open_ports.append(port)

    duration = time.time() - start_time
    print("--------------------------------------------------")
    print(f" Scan Complete in {duration:.2f} seconds. Open Ports Found: {len(open_ports)}")
    print(f" Open Ports List: {open_ports}")
    print("==================================================\n")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    scan_range(host, start, end)
