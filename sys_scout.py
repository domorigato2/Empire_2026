import socket
import platform
import os

def system_recon():
    print("\n==================================================")
    print("      CHASSIS TELEMETRY // LOCAL HOST RECON       ")
    print("==================================================")
    
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = "127.0.0.1"
        
    os_name = platform.system()
    os_release = platform.release()
    processor = platform.processor()
    
    print(f" Hostname      : {hostname}")
    print(f" Local IPv4    : {local_ip}")
    print(f" OS Platform   : {os_name} {os_release}")
    print(f" CPU Arch      : {processor}")
    print(f" Working Dir   : {os.getcwd()}")
    print("--------------------------------------------------")
    print(" STATUS: LOCAL HARDWARE PROFILED AND VERIFIED.")
    print("==================================================\n")

if __name__ == "__main__":
    system_recon()
