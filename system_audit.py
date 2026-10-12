import os
import psutil # Note: Ensure psutil is installed with 'pip install psutil'
import platform
import datetime

def run_audit():
    print("\n==================================================")
    print("      OPERATIONAL HEALTH // SYSTEM AUDIT          ")
    print("==================================================")
    print(f" Timestamp : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("--------------------------------------------------")
    
    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f" [+] CPU Load    : {cpu_usage}%")
    
    # RAM
    ram = psutil.virtual_memory()
    print(f" [+] RAM Used    : {ram.percent}% ({ram.used // (1024**2)} MB / {ram.total // (1024**2)} MB)")
    
    # Disk
    disk = psutil.disk_usage('/')
    print(f" [+] Disk Usage  : {disk.percent}% ({disk.free // (1024**3)} GB Free)")
    
    # Network
    net = psutil.net_io_counters()
    print(f" [+] Net Sent    : {net.bytes_sent // 1024} KB")
    print(f" [+] Net Recv    : {net.bytes_recv // 1024} KB")
    
    print("==================================================\n")

if __name__ == "__main__":
    try:
        run_audit()
    except ImportError:
        print("[!] Dependency Error: 'psutil' module missing.")
        print("[!] Run 'pip install psutil' to enable system monitoring.")
