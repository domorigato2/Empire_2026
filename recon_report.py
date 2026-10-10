import socket
import subprocess
import json
import sys
import datetime
import os

def generate_report(target):
    print("\n==================================================")
    print("      NOC AUTOMATION // JSON RECON REPORT         ")
    print("==================================================")
    print(f" Target Object : {target}")
    print(" Compiling reconnaissance telemetry dataset...")
    print("--------------------------------------------------")

    report = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target": target,
        "resolved_ip": None,
        "hostname": None,
        "ping_status": False,
        "open_ports": []
    }

    # 1. Resolve IP / Hostname
    try:
        resolved_ip = socket.gethostbyname(target)
        report["resolved_ip"] = resolved_ip
        try:
            hostname, _, _ = socket.gethostbyaddr(resolved_ip)
            report["hostname"] = hostname
        except socket.herror:
            report["hostname"] = "N/A"
    except socket.gaierror:
        print(f"[!] Target resolution failed for '{target}'.")
        return

    # 2. Ping check
    cmd = ["ping", "-n", "1", "-w", "500", resolved_ip]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    report["ping_status"] = (res.returncode == 0)

    # 3. Quick port probe (Common enterprise ports)
    common_ports = [21, 22, 53, 80, 443, 8080, 3389]
    for port in common_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            if s.connect_ex((resolved_ip, port)) == 0:
                report["open_ports"].append(port)
            s.close()
        except Exception:
            pass

    # Ensure Config directory exists for JSON artifacts
    if not os.path.exists("Config"):
        os.makedirs("Config")
        
    filename = f"Config/recon_{target.replace('.', '_')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print(f" [+] Recon data successfully serialized to: {filename}")
    print("--------------------------------------------------")
    print(json.dumps(report, indent=4))
    print("==================================================\n")

if __name__ == "__main__":
    t = sys.argv[1] if len(sys.argv) > 1 else "1.1.1.1"
    generate_report(t)
