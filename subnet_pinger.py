import ipaddress
import subprocess
import sys
import concurrent.futures

def ping_host(ip):
    # Fast 300ms timeout probe
    cmd = ["ping", "-n", "1", "-w", "300", str(ip)]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return str(ip), (res.returncode == 0)

def scan_subnet(cidr):
    print("\n==================================================")
    print("      SUBNET PINGER // LIVE HOST DISCOVERY        ")
    print("==================================================")
    print(f" Target CIDR    : {cidr}")
    print(" Generating host inventory and probing lines...")
    print("--------------------------------------------------")

    try:
        net = ipaddress.ip_network(cidr, strict=False)
    except ValueError as e:
        print(f"[!] Invalid CIDR: {e}")
        return

    hosts = list(net.hosts())
    print(f" Total Usable Hosts to Probe: {len(hosts)}")
    print("--------------------------------------------------")

    active_nodes = []
    # Multi-threaded concurrent execution engine (20 parallel threads)
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(ping_host, hosts)
        for ip, is_alive in results:
            if is_alive:
                print(f" [+] HOST ONLINE  : {ip}")
                active_nodes.append(ip)

    print("--------------------------------------------------")
    print(f" Scan Complete. Active Hosts Found: {len(active_nodes)}")
    print("==================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.0/28"
    scan_subnet(target)
