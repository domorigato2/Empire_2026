import subprocess
import sys
import concurrent.futures

def ping_single(ip):
    # 1 probe, 500ms timeout
    cmd = ["ping", "-n", "1", "-w", "500", ip]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ip, (res.returncode == 0)

def sweep_lan(base_subnet="192.168.1", start_host=1, end_host=15):
    print("\n==================================================")
    print("      MULTI-THREADED LAN DISCOVERY SWEEPER        ")
    print("==================================================")
    print(f" Subnet Target : {base_subnet}.{start_host} -> {base_subnet}.{end_host}")
    print(" Firing concurrent ICMP probes...")
    print("--------------------------------------------------")

    ips = [f"{base_subnet}.{i}" for i in range(start_host, end_host + 1)]
    active_hosts = []

    # Concurrency engine: 10 parallel worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(ping_single, ips)
        for ip, is_alive in results:
            if is_alive:
                print(f" [+] NODE ALIVE : {ip:<15} [RESPONDING]")
                active_hosts.append(ip)
            else:
                print(f" [-] NODE DEAD  : {ip:<15} [NO RESPONSE]")

    print("--------------------------------------------------")
    print(f" Sweep Complete: {len(active_hosts)} Active Nodes Detected.")
    print("==================================================\n")

if __name__ == "__main__":
    subnet = sys.argv[1] if len(sys.argv) > 1 else "192.168.1"
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 15
    sweep_lan(subnet, start, end)
