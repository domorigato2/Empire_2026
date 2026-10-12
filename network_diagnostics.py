# Save as network_diagnostics.py in C:\Users\sheil\Empire_2026\
import subprocess
import platform

def check_host(host_ip):
    print("\n" + "="*60)
    print(f" NETWORK TELEMETRY // PING SWEEP: {host_ip}")
    print("="*60)
    
    # Determine OS flag for ping count
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host_ip]
    
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
        if output.returncode == 0:
            print(f" [OK] Host {host_ip} is UP and responding.")
            status = "ONLINE"
        else:
            print(f" [!] Host {host_ip} timed out or unreachable.")
            status = "OFFLINE"
    except subprocess.TimeoutExpired:
        print(f" [X] Ping to {host_ip} timed out.")
        status = "TIMEOUT"
    
    print("="*60 + "\n")
    return status

if __name__ == "__main__":
    # Test against local gateway simulation or loopback
    check_host("127.0.0.1")